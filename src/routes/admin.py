from flask import Blueprint, abort, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from controllers.amenities import create_amenity, update_amenity, delete_amenity
from controllers.cities import create_city, update_city, delete_city
from controllers.places import create_place, delete_place, update_place
from controllers.users import create_user, update_user, delete_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.before_request
@jwt_required()
def check_admin():
    claims = get_jwt()
    if not claims.get('is_admin'):
        abort(403, "Administration rights required")

# Amenity block
@admin_bp.route('/admin/amenities', methods=['POST'])
def admin_create_amenity():
    return jsonify(create_amenity()), 201

@admin_bp.route('/admin/amenities/<amenity_id>', methods=['PUT'])
def admin_update_amenity(amenity_id):
    return jsonify(update_amenity(amenity_id))

@admin_bp.route('/admin/amenities/<amenity_id>', methods=['DELETE'])
def admin_delete_amenity(amenity_id):
    delete_amenity(amenity_id)
    return '', 204

# City block
@admin_bp.route('/admin/cities', methods=['POST'])
def admin_create_city():
    return jsonify(create_city()), 201

@admin_bp.route('/admin/cities/<city_id>', methods=['PUT'])
def admin_update_city(city_id):
    return jsonify(update_city(city_id))

@admin_bp.route('/admin/cities/<city_id>', methods=['DELETE'])
def admin_delete_city(city_id):
    delete_city(city_id)
    return '', 204

# Place block
@admin_bp.route('/admin/places', methods=['POST'])
def admin_create_place():
    return jsonify(create_place()), 201

@admin_bp.route('/admin/places/<place_id>', methods=['PUT'])
def admin_update_place(place_id):
    return jsonify(update_place(place_id))

@admin_bp.route('/admin/places/<place_id>', methods=['DELETE'])
def admin_delete_place(place_id):
    delete_place(place_id)
    return '', 204

# User block
@admin_bp.route('/admin/users', methods=['POST'])
def admin_create_user():
    return jsonify(create_user()), 201

@admin_bp.route('/admin/users/<user_id>', methods=['PUT'])
def admin_update_user(user_id):
    return jsonify(update_user(user_id))

@admin_bp.route('/admin/users/<user_id>', methods=['DELETE'])
def admin_delete_user(user_id):
    delete_user(user_id)
    return '', 204
