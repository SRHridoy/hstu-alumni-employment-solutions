from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://cjjwd1x74f1pcqc8izb7:pscale_pw_lcQFDBXqGnHi3TwHjuC3vlBNdyPgrNRrIf8Les2kmjT@ap-south.connect.psdb.cloud/hstuaes?charset=utf8mb4"

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
