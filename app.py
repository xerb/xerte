from flask import Flask, request,


app = Flask(__name__)


@app.route("/")
def index():
    return "Hot Dog!"

@app.route("/start_job", methods=["POST"])
def start_job():
    return print(request)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
