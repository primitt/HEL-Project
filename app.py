import flask
from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return flask.send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(port=5055)

