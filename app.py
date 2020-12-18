from flask import Flask , render_template, jsonify, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Control will come here and then gets redirect to the index function
@app.route("/")
def home():
	return redirect(url_for('index'))

@app.route("/index", methods = ["GET", "POST"])
def index():
	if request.method == 'POST': # When a user clicks submit button it will come here.
		data = request.form # gets the data from the form in index.html file
		name = data["name"]
		email = data["email"]

		user_data = [{"name":name, "email":email}] # stores them into a dictionary

		return render_template("index.html", user_data = user_data) # passes user_data variable into the index.html file.

	return render_template("index.html")

if __name__=="__main__":
	app.run(debug=True)
