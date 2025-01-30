from flask import Blueprint, request, jsonify
from src.services.user_service import UserService
import asyncio
import aiohttp

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/users', methods=['GET'])
async def get_users():
    users = await user_service.get_all_users()
    return jsonify(users), 200

@user_controller.route('/users/<int:user_id>', methods=['GET'])
async def get_user(user_id):
    user = await user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'User not found'}), 404

@user_controller.route('/users', methods=['POST'])
async def create_user():
    data = await request.get_json()
    user_id = await user_service.create_user(data['username'], data['email'], data['password'], data['role'])
    if user_id:
        return jsonify({'user_id': user_id}), 201
    return jsonify({'message': 'User creation failed'}), 400

@user_controller.route('/users/<int:user_id>', methods=['PUT'])
async def update_user(user_id):
    data = await request.get_json()
    success = await user_service.update_user(user_id, data.get('username'), data.get('email'), data.get('role'))
    if success:
        return jsonify({'message': 'User updated successfully'}), 200
    return jsonify({'message': 'User update failed'}), 400

@user_controller.route('/users/<int:user_id>', methods=['DELETE'])
async def delete_user(user_id):
    success = await user_service.delete_user(user_id)
    if success:
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User deletion failed'}), 400
