from flask import Flask, request
from urllib import parse


app = Flask(__name__)


@app.route("/")
def index():
    return "Hot Dog!"


@app.route("/start_job", methods=["POST"])
def start_job():
    params = request.args
    input_file_url = params['url']
    decode = parse.unquote(input_file_url)
    return decode



def urlencode(str):
    return parse.quote(str)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
