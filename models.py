import psycopg2

def dbcontaction():
	dbcon = 'dbname=challenge3 user=postgres password=refuge host=localhost'
	try:
		return psycopg2.connect(dbcon)
	except:
		print("Database connection failed")
