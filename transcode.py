from flask import request
from urllib import parse
import subprocess
import threading
import uuid

def start_tasks():
    params = request.args
    input_file_url = params['url']
    decode = parse.unquote(input_file_url)
    output_uuid = uuid.uuid4()
    start_transcode_pipeline(decode, output_uuid)
    return str(output_uuid), 201


def urlencode(str):
    return parse.quote(str)


def start_transcode_pipeline(url, uuid):
    ffmpeg_thread = threading.Thread(target=run_ffmpeg, args=(url, uuid))
    ffmpeg_thread.start()


def run_ffmpeg(url, uuid):
    output_file = '{}.avi'.format(uuid)
    try:
        subprocess.run(
                ['ffmpeg', '-i', url, output_file],
                check=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print('Calling ffmpeg failed')
        return

    return output_file
