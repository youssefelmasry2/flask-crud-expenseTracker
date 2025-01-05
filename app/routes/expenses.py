from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import Expense, User
from app.extensions import db

expenses_ns = Namespace('expenses', description='Expense operations')

# Request/response models
expense_model = expenses_ns.model('Expense', {
    'id': fields.Integer(readOnly=True, description='The expense unique identifier'),
    'description': fields.String(required=True, description='The expense description'),
    'amount': fields.Float(required=True, description='The expense amount')
})

@expenses_ns.route('/')
class ExpenseList(Resource):
    @jwt_required()
    @expenses_ns.marshal_list_with(expense_model)
    def get(self):
        """Get all expenses for the current user"""
        user_id = get_jwt_identity()
        return Expense.query.filter_by(user_id=user_id).all()

    @jwt_required()
    @expenses_ns.expect(expense_model)
    @expenses_ns.marshal_with(expense_model)
    def post(self):
        """Create a new expense"""
        user_id = get_jwt_identity()
        data = expenses_ns.payload
        new_expense = Expense(description=data['description'], amount=data['amount'], user_id=user_id)
        db.session.add(new_expense)
        db.session.commit()
        return new_expense, 201

@expenses_ns.route('/<int:expense_id>')
class ExpenseDetail(Resource):
    @jwt_required()
    @expenses_ns.marshal_with(expense_model)
    def get(self, expense_id):
        """Get a specific expense"""
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first_or_404()
        return expense

    @jwt_required()
    @expenses_ns.expect(expense_model)
    @expenses_ns.marshal_with(expense_model)
    def put(self, expense_id):
        """Update a specific expense"""
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first_or_404()
        data = expenses_ns.payload
        expense.description = data['description']
        expense.amount = data['amount']
        db.session.commit()
        return expense

    @jwt_required()
    def delete(self, expense_id):
        """Delete a specific expense"""
        user_id = get_jwt_identity()
        expense = Expense.query.filter_by(id=expense_id, user_id=user_id).first_or_404()
        db.session.delete(expense)
        db.session.commit()
        return 'deleted', 204