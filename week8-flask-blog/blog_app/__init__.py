import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login = LoginManager()

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.getcwd(), "templates")
    )

    app.config.from_object(Config)

    db.init_app(app)
    login.init_app(app)

    from blog_app.auth.routes import auth
    from blog_app.main.routes import main
    from blog_app.posts.routes import posts

    app.register_blueprint(auth)
    app.register_blueprint(main)
    app.register_blueprint(posts)

    return app
