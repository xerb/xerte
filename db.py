import psycopg2 # TODO: add to requirements or RUN in docker file? Tested with psycopg = 2-2.7.7
import time


def connect_db():
    """Connect to Database with environment variables and pass connection to other functions."""
    conn = psycopg2.connect( # TODO: Replace with environ variables.
        host="localhost",
        database="transcode", 
        user="j",
        password="postgres"
        )
    cur = conn.cursor()
    # cur.execute('''CREATE TABLE IF NOT EXISTS job_status (uuid, url, status, start_time, stop_time)''')
    return conn

def insert_job_status(uuid, url):
    """Create new row in database."""
    db = connect_db()
    cur = db.cursor()
    sql = "INSERT INTO job_status(uuid, url, status, start_time, stop_time) \
        VALUES (%(uuid)s, %(url)s, %(status)s, %(start_time)s, %(stop_time)s)"
    cur.execute(sql, {'uuid':uuid, 'url':url, 'status':'Started', 'start_time':time.time(), 'stop_time':None})
    db.commit()
    db.close

def update_job_status(uuid, status):
    """Update row in database"""
    db = connect_db()
    cur = db.cursor()
    sql = "UPDATE job_status SET status=%(status)s, stop_time=%(stop_time)s WHERE uuid=%(uuid)s;"
    cur.execute(sql, {'status':status, 'stop_time':time.time(), 'uuid':uuid})
    db.commit()
    db.close()

def get_job_status(uuid):
    """Database query for status returned. Json compatible."""
    db = connect_db()
    cur = db.cursor()
    sql = "SELECT status, start_time, stop_time FROM job_status WHERE uuid=%(uuid)s;"
    results = cur.execute(sql, {'uuid':uuid,}) # TODO: WHAT???? How does this line and the next run correctly?
    r = cur.fetchone()
    if not r:
        return None
    
    data = {
        'status':r[0],
        'start_time':r[1],
        'stop_time':r[2]
    }
    db.close()
    return data
 