from flask import Flask
from config import Config
from .models import db, migrate
from .controllers import bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    return app