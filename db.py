import sqlite3
import time

def get_db():
    """Creates a database if needed and returns a connection to it."""
    conn = sqlite3.connect('status.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS job_status (uuid, url, status, started, stopped)''')
    
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
    c.execute("UPDATE job_status SET status=(?), stopped=(?) WHERE uuid=?", (status, time.time(), uuid))
    db.commit()
    db.close()

def get_job_status(uuid):
    db = get_db()
    c = db.cursor()
    results = c.execute("SELECT status FROM job_status WHERE uuid=?", (uuid,))
    status = results.fetchone()[0]
    db.close()
    return status
