from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import os

app = Flask(__name__)
boot = Bootstrap(app=app)
# Not really needed for the demo but good practice
app.config['SECRET_KEY'] = os.urandom(12).hex()

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == "__main__":
	app.run()