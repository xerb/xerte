from flask import Flask, request
from urllib import parse
import subprocess
import threading
import uuid


app = Flask(__name__)


@app.route("/")
def index():
    return "Hot Dog!"


@app.route("/start_job", methods=["POST"])
def start_job():
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
