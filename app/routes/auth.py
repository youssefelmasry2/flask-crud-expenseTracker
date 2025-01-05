from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

auth_ns = Namespace('auth', description='Authentication operations')

# Request/response models
user_model = auth_ns.model('User', {
    'username': fields.String(required=True, description='The user username'),
    'password': fields.String(required=True, description='The user password')
})

@auth_ns.route('/register')
class Register(Resource):
    @auth_ns.expect(user_model)
    def post(self):
        """Register a new user"""
        data = auth_ns.payload
        username = data['username']
        password = generate_password_hash(data['password'])

        if User.query.filter_by(username=username).first():
            return {'message': 'Username already exists'}, 400

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully'}, 201

@auth_ns.route('/login')
class Login(Resource):
    @auth_ns.expect(user_model)
    def post(self):
        """Login and get an access token"""
        data = auth_ns.payload
        user = User.query.filter_by(username=data['username']).first()

        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401