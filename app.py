from flask import Flask, request
from urllib import parse
import subprocess
import threading


app = Flask(__name__)


@app.route("/")
def index():
    return "Hot Dog!"


@app.route("/start_job", methods=["POST"])
def start_job():
    params = request.args
    input_file_url = params['url']
    decode = parse.unquote(input_file_url)
    start_transcode_pipeline(decode)
    return 'Created', 201


def urlencode(str):
    return parse.quote(str)


def start_transcode_pipeline(url):
    print(url)
    ffmpeg_thread = threading.Thread(target=run_ffmpeg, args=(url,))
    ffmpeg_thread.start()


def run_ffmpeg(url):
    output_file = 'output.avi'
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
