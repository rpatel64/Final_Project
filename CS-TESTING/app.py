#!/usr/bin/env python3
import psycopg2

from flask import Flask, render_template, request
app = Flask(__name__)

#import dj_database_url

#conn = psycopg2.connect("host=ec2-23-23-92-204.compute-1.amazonaws.com dbname=d1fs1cm170ct9t user=gxupvblzzfulmn password=6f218f9e00cb85e2d96043b8a25898951fd0fbd475a5bcbeb9eb2ba4cc42d072")
#cur = conn.cursor()

#email = request.values.get('email')

#email = raw_input('Please enter your email: ')
#password = raw_input('Please enter your password: ')
#firstName = raw_input('Please enter your first name: ')
#lastName = raw_input('Please enter your last name: ')

#insert_query = "INSERT INTO members VALUES('" + str(email) + "', '" + str(password) + "', '" + str(firstName) + "', '" + str(lastName) + "')"

#cur.execute(insert_query)

#print 'Thank you for creating an account with Fit Your Fit ' + str(firstName) + ' ' + str(lastName)
#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
#conn.commit()

@app.route('/')
def student():
   return render_template('login.html')

@app.route('/SignUp.html')
def signup():
    return render_template('SignUp.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
