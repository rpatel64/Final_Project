from flask import Flask, request, render_template, redirect, url_for, request
import psycopg2
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/Login.html', methods=['GET','POST'])
def login():
	#error = NONE	i
	#sprint(request.form.get('username')
	print(request.values.get("password"))
	if request.form.get('username') != 'admin' or request.form.get('password') != 'admin':
		print("1")
		print(request)
		print(request.values.get("username"))
		print(request.values.get("password"))
		if request.form.get('username') == "hello":
			print("hello")
	else: 
		print("2")
		return redirect(url_for('/'))
	print("3")
	return render_template('/Login.html')

@app.route("/result",methods=['GET','POST'])
def result():
	print(request.form.get("username"))
	print(request.values.get("username"))
	print(request.values.get("password"))
	return render_template('index.html')

@app.route('/index.html')
def index():
	return render_template('index.html')

@app.route('/SignUp.html', methods=['GET','POST'])
def signup():
	if request.values.get('firstname') != None:
		firstName = request.values.get('firstname')
		lastName = request.values.get('lastname')
		password = request.values.get('password')
		print(request.values.get('confirm'))
		email = request.values.get('email')
	
		conn = psycopg2.connect("host=ec2-23-23-92-204.compute-1.amazonaws.com dbname=d1fs1cm170ct9t user=gxupvblzzfulmn password=6f218f9e00cb85e2d96043b8a25898951fd0fbd475a5bcbeb9eb2ba4cc42d072")
		cur = conn.cursor()

		insert_query = "INSERT INTO members VALUES('" + str(email) + "', '" + str(password) + "', '" + str(firstName) + "', '" + str(lastName) + "')"

		cur.execute(insert_query)
		conn.commit()







	return render_template('SignUp.html')
	

if __name__ == '__main__':
	app.run(debug=True)	
