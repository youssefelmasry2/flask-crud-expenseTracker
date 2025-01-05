from flask import Flask
from app.extensions import db
from flask_restx import Api

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    
     # Register blueprints
    
     # Set up Flask-RESTx API
    api = Api(app, version='1.0', title='Flask CRUD API',
              description='A simple CRUD API with PostgreSQL and Flask.')

    # Register namespaces
    from app.routes import main_ns
    api.add_namespace(main_ns, path='/')

    # Create database tables (useful during development)
    with app.app_context():
        db.create_all()

    return app
