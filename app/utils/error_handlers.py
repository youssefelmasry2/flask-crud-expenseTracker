from flask import jsonify
from flask_restx import Api

api = Api(version='1.0', title='Expense Tracker API', description='An API for managing expenses' , doc='/doc')

@api.errorhandler
def default_error_handler(e):
    """Default error handler"""
    return {'message': str(e)}, getattr(e, 'code', 500)