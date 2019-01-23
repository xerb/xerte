from flask import Flask, request
from urllib import parse
import uuid
import transcode
import json
from db import get_job_status

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


@app.route("/job_status/<uuid:uuid>", methods=["GET"])
def job_status(uuid):
    """DB query for job status"""
    uuid = str(uuid)
    result = get_job_status(uuid)
    data = json.dumps(result)
    data = data or "Not Found"
    http_code = 200 if result else 404
    return data, http_code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
