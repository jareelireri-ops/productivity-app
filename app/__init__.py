from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productivity.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'super_secret_key' # Required for Sessions

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    ma.init_app(app)

    from app.models.user import User
    from app.models.task import Task

    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    from app.routes.tasks import tasks_bp
    app.register_blueprint(tasks_bp)

    return app