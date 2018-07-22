from app import app
@app.route('/')
def home():
	return "Start Now Create Your Diaries"


@app.route('/api/v1/refuge', methods=['GET'])
def about():
	return "yes am refuge wise"