from flask import Flask, jsonify, render_template, request
from flask_compress import Compress
from flask_cors import CORS
from waitress import serve
from proto import *


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

Compress(app)
CORS(app, resource={"/*": {"origins": "*"}})

log = putlog("MainExecutor")

configFile = "config/app.setting.json"
configuration = readJson(configFile)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("error/500.html"), 500


@app.errorhandler(403)
def page_forbidden(e):
    return render_template("error/403.html"), 403


@app.route('/', methods = ['POST', 'GET'])
def render_page():
    return render_template("app/application.html")


if __name__ == "__main__":
    if configuration["App"]["Mode"] == 0:
        app.run(host=configuration["App"]["Host"],
                port=configuration["App"]["Port"],
                debug=True,
                threaded=True)
    else:
        serve(app, host=configuration["App"]["Host"],
                port=configuration["App"]["Port"])
