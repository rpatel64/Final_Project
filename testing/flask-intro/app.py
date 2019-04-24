#!/usr/bin/env python3
from flask import Flask, request, render_template, redirect, url_for, request
import psycopg2
import re
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Login.html', methods=['GET','POST'])
def login():
    bool1 = False
    bool2 = False
    error = None
    username = request.values.get('username')
    password = request.values.get("password")

    conn = psycopg2.connect("host=ec2-23-23-92-204.compute-1.amazonaws.com dbname=d1fs1cm170ct9t user=gxupvblzzfulmn password=6f218f9e00cb85e2d96043b8a25898951fd0fbd475a5bcbeb9eb2ba4cc42d072")
    cur = conn.cursor()

    cur.execute("SELECT email FROM members")
    user = cur.fetchall()
    for i in user:
        #	print(i, username)
        if username in i:
            bool1 = True

    cur.execute("SELECT password FROM members")
    passw = cur.fetchall()

    for j in passw:
        #	print(j, password)
        if password in j:
            bool2 = True

    if bool1 == True and bool2 == True:
        return render_template('/index.html')
    else:
        if username != None and password != None:
            error = "Invalid Email or Password"

    return render_template('/Login.html',error = error)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/UpperBody_Main.html')
def upper():
    return render_template('UpperBody_Main.html')

@app.route('/LowerBody_Main.html')
def lower():
    return render_template('LowerBody_Main.html')

@app.route('/Cardio_Main.html')
def cardio():
    return render_template('Cardio_Main.html')

@app.route('/SignUp.html', methods=['GET','POST'])
def signup():
    error = None;
    if request.values.get('firstname') != None:
        firstName = request.values.get('firstname')
        lastName = request.values.get('lastname')
        password = request.values.get('password')
        confirm = request.values.get('confirm')
        email = request.values.get('email')

        if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
            error = 'Invalid Email address, please try again.'
            return render_template('SignUp.html', error = error)
        else:
            if password == confirm:
                conn = psycopg2.connect("host=ec2-23-23-92-204.compute-1.amazonaws.com dbname=d1fs1cm170ct9t user=gxupvblzzfulmn password=6f218f9e00cb85e2d96043b8a25898951fd0fbd475a5bcbeb9eb2ba4cc42d072")
                cur = conn.cursor()

                insert_query = "INSERT INTO members VALUES('" + str(email) + "', '" + str(password) + "', '" + str(firstName) + "', '" + str(lastName) + "')"

                cur.execute(insert_query)
                conn.commit()
                Error = None
                return render_template('Login.html')
            else:
                if password != None and confirm != None:
                    error = 'Passwords did not match, please try again.'
                    return render_template('SignUp.html',error = error)

    return render_template('SignUp.html')


if __name__ == '__main__':
    app.run(debug=True)
