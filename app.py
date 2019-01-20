from flask import Flask, request
from urllib import parse
import uuid
import transcode


app = Flask(__name__)


@app.route("/start_job", methods=["POST"])
def start_job():
    """POST media file to be converted.
    HTML decoding built in.
    Responce will be a generated UUID which will correspond to created file name.
    """

    params = request.args
    input_file_url = params['url']
    decode = parse.unquote(input_file_url)
    output_uuid = uuid.uuid4()
    transcode.start_transcode_pipeline(decode, output_uuid)
    return str(output_uuid), 201


@app.route("/job_status", methods=["POST"]) # TODO Or a GET?
def job_status():
    """GET request with UUID to track if media is converted.
    """
    params = request.args
    thread_name = params['uuid']
    decode = parse.unquote(thread_name)
    status = transcode.check_status(decode)


    return status, 201 # TODO change this to the correct response 


if __name__ == "__main__":V
    app.run(host='0.0.0.0', port=8080, debug=True)
