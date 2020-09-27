
from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin.contrib.sqla import ModelView

from flask_admin import Admin


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

from models import *
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))
