from sqlalchemy import create_engine, text
import os
#.....data
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})
#last masti....please forgive me

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
  for row in result.all():
    jobs.append(row._asdict())
  return jobs


def load_job_from_db(id):
    with engine.connect() as conn:
        stmt = text("SELECT * FROM jobs WHERE id = :id")
        result = conn.execute(stmt, {"id": id})
        row = result.fetchone()
        result.close()
        if row is None:
            return None
        else:
            return dict(zip(result.keys(), row))



def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

        conn.execute(
            query.bindparams(
                job_id=job_id,
                full_name=data['full_name'],
                email=data['email'],
                linkedin_url=data['linkedin_url'],
                education=data['education'],
                work_experience=data['work_experience'],
                resume_url=data['resume_url']
            )
        )






  