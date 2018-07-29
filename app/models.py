import psycopg2
#import datetime

dbcon = psycopg2.connect(dbname='diary', user='postgres', password='refuge', host='localhost')
	#try:
	#	return psycopg2.connect(dbcon)
	#except:
		#print("Database connection failed")

try:
	dbcur = dbcon.cursor()
	dbcur.execute('''CREATE TABLE users(
		id 	   SERIAL,
		full_name    VARCHAR(25) NOT NULL,
		username     VARCHAR(25) NOT NULL,
		email        VARCHAR(100) NOT NULL,
		password     VARCHAR(255) NOT NULL,
		last_login   timestamp DEFAULT CURRENT_TIMESTAMP,
		PRIMARY KEY (id)
		);''')
	dbcon.commit()
	#print ('Table is already exist')
except:
	print ('Table is already exist')


try:
	dbcur = dbcon.cursor()
	dbcur.execute('''CREATE TABLE entries(
		id    SERIAL,
		user_id   INT,
		title     VARCHAR(25)  NOT NULL,
		dates     VARCHAR(25)   NOT NULL,
		entries   VARCHAR(500)   NOT NULL,
		created_at timestamp DEFAULT CURRENT_TIMESTAMP,
		FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
		);''')
	dbcon.commit()
except:
		print ('Table is already exist')

