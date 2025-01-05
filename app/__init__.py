from flask import Flask
from flask_restx import Api
from app.extensions import db, jwt
from app.routes.auth import auth_ns
from app.routes.expenses import expenses_ns
from app.utils.error_handlers import api

# Define the authorization scheme
authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'Enter your JWT token in the format: Bearer <token>'
    }
}

# Initialize the Api object with authorizations
api = Api(
    version='1.0',
    title='Expense Tracker API',
    description='An API for managing expenses',
    doc='/swagger/',  # Swagger UI endpoint
    authorizations=authorizations,  # Add authorization scheme
    security='Bearer Auth'  # Enable security globally
)

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    api.init_app(app)

    # Register namespaces
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(expenses_ns, path='/expenses')

    # Create database tables
    with app.app_context():
        db.create_all()

    return app