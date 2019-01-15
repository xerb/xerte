from flask import Flask, request
from urllib import parse
import uuid
import transcode


app = Flask(__name__)


@app.route("/start_job", methods=["POST"])
def start_job():
    params = request.args
    input_file_url = params['url']
    decode = parse.unquote(input_file_url)
    output_uuid = uuid.uuid4()
    transcode.start_transcode_pipeline(decode, output_uuid)
    return str(output_uuid), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
