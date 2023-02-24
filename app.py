from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id' : 1,
    'tittle':'Data Analyst',
    'location':' Dhaka, Bangladesh',
    'salary':' 10,00,000 Tk',
  },
  {
    'id' : 2,
    'tittle':'AI Engineer',
    'location':' Dinajpur, Bangladesh',
    'salary':' 18,00,000 Tk',
  },
  {
    'id' : 3,
    'tittle':'Cloud Engineer',
    'location':' Remote',
    'salary':' 15,00,000 Tk',
  },
  {
    'id' : 4,
    'tittle':'Python Devloper',
    'location':'Rajshai, Bangladesh',
    'salary':' 12,00,000 Tk',
  },
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)