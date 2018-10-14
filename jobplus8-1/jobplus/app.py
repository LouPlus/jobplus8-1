from flask_migrate import Migrate
from flask import Flask, render_template, url_for
from .config import configs
from jobplus.models import db,User,Job,Company
from flask_login import LoginManager

def register_blueprints(app):
    from .handlers import front,admin,company,user,job
    app.register_blueprint(front)
    app.register_blueprint(admin)
    app.register_blueprint(user)
    app.register_blueprint(company)
    app.register_blueprint(job)
    

def create_app(config):
    app=Flask(__name__)
    app.config.from_object(configs.get(config))
    db.init_app(app)
    Migrate(app,db)
    register_blueprints(app)
    return app
