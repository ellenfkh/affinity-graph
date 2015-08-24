from flask import Flask, render_template, jsonify
from manage_data import load_from_file
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/data')
@app.route('/data/<filename>')
def load_jsonfy_data(filename=None):
    filepath = "data/" + filename
    return jsonify(load_from_file(filepath))


if __name__ == '__main__':
    app.run()
