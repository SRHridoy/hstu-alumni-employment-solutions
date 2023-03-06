from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})


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



