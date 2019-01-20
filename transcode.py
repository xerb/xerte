import subprocess
import threading
import sqlite3
import time


conn = sqlite3.connect('log.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS job_status (uuid, status, started, stopped)''')


def start_transcode_pipeline(url, uuid):
    """Kicks off new threads using the 'run_ffmpeg' function.
    """

    ffmpeg_thread = threading.Thread(target=run_ffmpeg, args=(url, uuid))
    ffmpeg_thread.start()


def run_ffmpeg(url, uuid):
    """Runs a thread for transcoding with ffmpeg software.
        Also creates a log tracking completion of threads.
    """
    output_file = '{}.avi'.format(uuid)
    try:
        c.execute("INSERT INTO job_status (?,?,?,?)", (uuid, "Started", time.time(), "None"))
        conn.commit() # TODO: Needed?
        subprocess.run(
                ['ffmpeg', '-i', url, output_file],
                check=True, stderr=subprocess.STDOUT)
        c.execute("UPDATE job_status SET status='Complete' stopped=? WHERE uuid=?", (time.time(), uuid))
        conn.commit()
    except subprocess.CalledProcessError:
        c.execute("INSERT INTO job_status (?,?,?,?)", (uuid, "Failed", time.time(), time.time()))
        conn.commit()
        print('Calling ffmpeg failed')
        return

    return output_file
