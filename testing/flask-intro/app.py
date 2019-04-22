from flask import Flask, request, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/Login.html', methods=['GET','POST'])
def login():
	#error = NONE	
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			baby = 1
			print("1")
		else: 
			return redirect(url_for('/'))
			print("2")
	return render_template('/Login.html')

@app.route('/index.html')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)	
