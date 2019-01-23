import sqlite3
import time

def get_db():
    """Creates a database if needed and returns a connection to it."""
    conn = sqlite3.connect('status.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS job_status (uuid, url, status, start_time, stop_time)''')
    
    return conn

def insert_job_status(uuid, url):
    """Create new row in database"""
    db = get_db()
    c = db.cursor()
    c.execute("INSERT INTO job_status VALUES (?,?,?,?,?)", (uuid, url, "STARTED", time.time(), None))
    db.commit()
    db.close()

def update_job_status(uuid, status):
    """Update row in database"""
    db = get_db()
    c = db.cursor()
    c.execute("UPDATE job_status SET status=(?), stop_time=(?) WHERE uuid=?", (status, time.time(), uuid))
    db.commit()
    db.close()

def get_job_status(uuid):
    db = get_db()
    c = db.cursor()
    results = c.execute("SELECT status, start_time, stop_time FROM job_status WHERE uuid=?", (uuid,))
    r = results.fetchone()
    if not r:
        return None

    data = {
            'status': r[0],
            'start_time': r[1],
            'stop_time': r[2]
            }
    db.close()
    return data
