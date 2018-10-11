from flask import Flask
from .config import configs

def create_app(config):
	app = Flask(__name__)
	app.config.from_object(configs.get(config))

	@app.route('/test')
	def test():
		return 'This is test!!!!!!!!!!!!'

	return app
