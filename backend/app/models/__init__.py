from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()

from .Users import Users
from .Tasks import Tasks
from .Categories import Categories