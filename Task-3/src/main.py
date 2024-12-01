from flask import Flask, render_template, url_for, jsonify, request
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

@app.route("/getSingle", methods=["POST"])
def getSingle():
    name = request.get_json(force=True)
    city = requester.get_by_name(name)
    single_json = json.dumps(city)
    return jsonify(single_json)

@app.route("/getFive", methods=["POST"])
def getFive():
	amount = request.get_json()
	cities = requester.collect_cities(int(amount))
	cities_json = json.dumps(cities)
	return jsonify(cities_json)

if __name__ == "__main__":
	app.run()