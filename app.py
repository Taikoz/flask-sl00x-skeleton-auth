from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db
from routes import routes
from dotenv import load_dotenv
from flask_migrate import Migrate
import os

def create_app():
    load_dotenv()
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')
    app = Flask(__name__)
    migrate = Migrate(app, db)
    wsgi_app = app.wsgi_app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + db_user + \
        ':' + db_password + '@' + db_host + ':'+db_port+'/' + db_name
    db.init_app(app)
    for route in routes:
        app.register_blueprint(route['blueprint'], url_prefix=route['prefix'])
    return app


if __name__ == '__main__':
    import os
    app = create_app()
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
