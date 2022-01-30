from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)
app.secret_key = "sulamabuza"

@app.route("/hello")
def index():
	#set initial message which will be changeable
	flash("what's your name?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("Hi " + str(request.form['name_input']) + ", great to see you")
	return  render_template("index.html")

#display a different message
