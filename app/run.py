from flask import Flask
from __init__ import api_bp


def create_app(config_filename):
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'refuge'

	app.register_blueprint(api_bp, url_prefix='/api')

	return app



if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True)
