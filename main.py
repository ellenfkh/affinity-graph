from flask import Flask, render_template
from manage_data import load_from_file
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/graph/<filename>')
def disply_graph(filename):
    json_data = load_from_file(filename)
    return render_template("graph.html", data=json_data)


if __name__ == '__main__':
    app.run()
