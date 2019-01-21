import subprocess
import threading
import time
from db import get_db, insert_job_status, update_job_status


def start_transcode_pipeline(url, uuid):
    """Kicks off new threads using the 'run_ffmpeg' function.
    """
    ffmpeg_thread = threading.Thread(target=run_ffmpeg, args=(url, uuid))
    ffmpeg_thread.start()


def run_ffmpeg(url, uuid):
    """Runs a thread for transcoding with ffmpeg software.
        Also creates a log tracking completion of threads.
    """
    name_uuid = str(uuid)
    output_file = '{}.avi'.format(uuid) # TODO: Remove hard-coding!
    insert_job_status(name_uuid, url)
    try:
        subprocess.run(
                ['ffmpeg', '-i', url, output_file],
                check=True, stderr=subprocess.STDOUT)
        update_job_status(name_uuid, "COMPLETE")
    except subprocess.CalledProcessError:
        update_job_status(name_uuid, "FAILED")
        return

    return output_file
