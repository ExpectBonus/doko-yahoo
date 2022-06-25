from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields

from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()

fields = fields.fields

def init_db(app):
    db.init_app(app)
    Migrate(app,db)