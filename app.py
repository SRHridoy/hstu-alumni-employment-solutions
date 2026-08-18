from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)


# Demo jobs — database unavailable হলে এগুলো দেখাবে
DEMO_JOBS = [
    {
        "id": 1,
        "title": "Software Engineer",
        "location": "Dhaka, Bangladesh",
        "company": "HSTU Alumni Solutions",
        "description": "Develop and maintain web applications using modern technologies."
    },
    {
        "id": 2,
        "title": "Frontend Developer",
        "location": "Remote",
        "company": "HSTU Alumni Solutions",
        "description": "Build responsive and user-friendly web interfaces."
    },
    {
        "id": 3,
        "title": "Backend Developer",
        "location": "Dhaka, Bangladesh",
        "company": "HSTU Alumni Solutions",
        "description": "Develop APIs and backend services for web applications."
    }
]


@app.route("/")
def hello_HAES():

    try:
        jobs_list = load_jobs_from_db()

        # Database connected but no jobs found
        if not jobs_list:
            jobs_list = DEMO_JOBS

    except Exception as e:
        print("Database unavailable:", e)

        # Database না থাকলেও website দেখাবে
        jobs_list = DEMO_JOBS

    return render_template("home.html", jobs=jobs_list)


@app.route("/api/jobs")
def list_jobs():

    try:
        jobs = load_jobs_from_db()

        if not jobs:
            jobs = DEMO_JOBS

    except Exception as e:
        print("Database unavailable:", e)
        jobs = DEMO_JOBS

    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):

    try:
        job = load_job_from_db(id)

    except Exception as e:
        print("Database unavailable:", e)

        # Demo job খুঁজবে
        job = next(
            (job for job in DEMO_JOBS if str(job["id"]) == str(id)),
            None
        )

    if not job:
        return "Not Found", 404

    return render_template("jobpage.html", job=job)


@app.route("/job/<id>/apply", methods=["POST"])
def apply_to_job(id):

    data = request.form

    try:
        job = load_job_from_db(id)

        if not job:
            job = next(
                (job for job in DEMO_JOBS if str(job["id"]) == str(id)),
                None
            )

        # Database available হলে application save করবে
        add_application_to_db(id, data)

    except Exception as e:
        print("Database unavailable. Application not saved:", e)

        # Demo mode-এ application শুধু page দেখানোর জন্য থাকবে
        job = next(
            (job for job in DEMO_JOBS if str(job["id"]) == str(id)),
            None
        )

    return render_template(
        "application_submitted.html",
        application=data,
        job=job
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )