from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/time')
def hello_world():
    time=datetime.datetime.now().strftime("%H:%M:%S")
    return time


app.run(host='0.0.0.0',
        port=8080,
        debug=True)