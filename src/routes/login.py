from flask import Blueprint
from src.controllers.users import (
    create_user,
    delete_user,
    get_user_by_id,
    get_users)
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    get_raw_jwt)
from flask import request, jsonify
from src.models.user import User


 
login_bp = Blueprint("login", __name__, url_prefix="/login")
 
login_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return 'Wrong username or password', 401