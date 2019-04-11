#!/usr/bin/env python3
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/Login.html')
def login():
	return render_template("Login.html")

if __name__ == '__main__':
	app.run(debug=True)
