from flask import Flask, render_template
import transcode

app = Flask(__name__, template_folder='template')


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/start_job", methods=["POST"])
def start_job():
   return transcode.start_tasks()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
