import psycopg2
import os
import time
from flask import current_app, g



def connect_db():
    """Connect to Database with environment variables and pass connection to
    other functions."""

    if 'db' not in g:
        g.db = psycopg2.connect(  # TODO: Replace with environ variables.
            host=os.environ['DBHOST'],
            database=os.environ['POSTDB'],
            user=os.environ['DBUSER'],
            password=os.environ['DBPASSWORD']
            )
    # cur.execute('''CREATE TABLE IF NOT EXISTS job_status (uuid, url, status, start_time, stop_time)''')
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def insert_job_status(uuid, url):
    """Create new row in database."""
    cur = g.db.cursor()
    sql = "INSERT INTO job_status(uuid, url, status, start_time, stop_time) \
        VALUES (%(uuid)s, %(url)s, %(status)s, %(start_time)s, %(stop_time)s)"
    cur.execute(sql,
                {
                    'uuid': uuid,
                    'url': url,
                    'status': 'Started',
                    'start_time': time.time(),
                    'stop_time': None
                })
    g.db.commit()


def update_job_status(uuid, status):
    """Update row in database"""
    cur = g.db.cursor()
    sql = "UPDATE job_status \
            SET status=%(status)s, stop_time=%(stop_time)s \
            WHERE uuid=%(uuid)s;"
    cur.execute(sql,
                {'status': status, 'stop_time': time.time(), 'uuid': uuid}
                )
    g.db.commit()


def get_job_status(uuid):
    """Database query for status returned. Json compatible."""
    cur = g.db.cursor()
    sql = "SELECT status, start_time, stop_time \
        FROM job_status WHERE uuid=%(uuid)s;"
    cur.execute(sql, {'uuid': uuid, })
    result = cur.fetchone()
    if not result:
        return None

    data = {
        'status': result[0],
        'start_time': result[1],
        'stop_time': result[2],
    }
    return data
