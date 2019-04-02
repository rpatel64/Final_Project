import psycopg2
conn = psycopg2.connect("host=ec2-23-23-92-204.compute-1.amazonaws.com dbname=d1fs1cm170ct9t user=gxupvblzzfulmn password=6f218f9e00cb85e2d96043b8a25898951fd0fbd475a5bcbeb9eb2ba4cc42d072")
cur = conn.cursor()

email = raw_input('Please enter your email: ')
password = raw_input('Please enter your password: ')
firstName = raw_input('Please enter your first name: ')
lastName = raw_input('Please enter your last name: ')

insert_query = "INSERT INTO members VALUES('" + str(email) + "', '" + str(password) + "', '" + str(firstName) + "', '" + str(lastName) + "')"

cur.execute(insert_query)

#print insert_query

print 'Account Creation Successful'

conn.commit()
