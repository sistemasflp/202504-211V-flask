from flask import Blueprint, jsonify, request
from app.models.user import (
    fetch_all_users,
    fetch_user_by_id,
    create_user as create_user_model,
    update_user as update_user_model,
    delete_user as delete_user_model,
)

users_bp = Blueprint("users", __name__, url_prefix="/users")


def _serialize_user(user_row):
    return {
        "id": user_row["id"],
        "username": user_row["username"],
        "email": user_row["email"],
        "password": user_row["password"],
    }


@users_bp.route("", methods=["GET"])
def get_all_users():
    users = fetch_all_users()
    return jsonify([_serialize_user(user) for user in users]), 200


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = fetch_user_by_id(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(_serialize_user(user)), 200


@users_bp.route("", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "username, email and password are required"}), 400

    user_id = create_user_model(username, email, password)
    user = fetch_user_by_id(user_id)
    return jsonify(_serialize_user(user)), 201


@users_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = fetch_user_by_id(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON body"}), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "username, email and password are required"}), 400

    update_user_model(user_id, username, email, password)
    updated_user = fetch_user_by_id(user_id)
    return jsonify(_serialize_user(updated_user)), 200


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = fetch_user_by_id(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404

    delete_user_model(user_id)
    return jsonify({"message": "User deleted successfully"}), 200
