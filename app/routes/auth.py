from flask import Blueprint, request, session, jsonify
from app import db
from app.models.user import User
from app.schemas.user_schema import user_schema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if User.query.filter_by(username=data.get('username')).first():
        return {"error": "Username already exists"}, 400

    new_user = User(username=data.get('username'))
    # Triggers Bcrypt hashing via the setter in models/user.py
    new_user.password_hash = data.get('password')

    db.session.add(new_user)
    db.session.commit()

    # Log in automatically
    session['user_id'] = new_user.id

    return user_schema.dump(new_user), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data.get('username')).first()

    # Uses the .authenticate method in models/user.py to check password
    if user and user.authenticate(data.get('password')):
        session['user_id'] = user.id
        return user_schema.dump(user), 200
    
    return {"error": "Invalid username or password"}, 401

@auth_bp.route('/logout', methods=['DELETE'])
def logout():
    session.pop('user_id', None)
    return {}, 204

@auth_bp.route('/check_session', methods=['GET'])
def check_session():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        return user_schema.dump(user), 200
    return {"error": "No user logged in"}, 401