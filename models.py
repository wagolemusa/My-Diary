import psycopg2
#import datetime

dbcon = psycopg2.connect(dbname='mydiary', user='postgres', password='refuge', host='localhost')
	#try:
	#	return psycopg2.connect(dbcon)
	#except:
		#print("Database connection failed")

try:
	dbcur = dbcon.cursor()
	dbcur.execute('''CREATE TABLE users(
		user_id 	   SERIAL PRIMARY KEY,
		full_name    TEXT NOT NULL,
		username     TEXT NOT NULL,
		email        TEXT NOT NULL,
		password     TEXT NOT NULL,
		created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
		);''')
	dbcon.commit()
	#print ('Table is already exist')
except:
	print ('Table is already exist')


try:
	dbcur = dbcon.cursor()
	dbcur.execute('''CREATE TABLE entries(
		id    SERIAL PRIMARY KEY,
		user_id   INT,
		title     TEXT   NOT NULL,
		dates     TEXT   NOT NULL,
		entries   TEXT   NOT NULL,
		created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP


		);''')
	dbcon.commit()
except:
		print ('Table is already exist')

