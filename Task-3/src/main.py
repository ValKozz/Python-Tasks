from flask import Flask, render_template, url_for, jsonify
import json
from flask_bootstrap import Bootstrap
from make_requests import MakeRequests
import os

app = Flask(__name__)
boot = Bootstrap(app=app)
# Not really needed for the demo but good practice
app.config['SECRET_KEY'] = os.urandom(12).hex()
requester = MakeRequests()

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/getFive")
def getFive():
	cities = requester.collect_cities()
	# For debug
	cities_json = json.dumps(cities)
	return jsonify(cities_json)

if __name__ == "__main__":
	app.run()