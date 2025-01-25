from flask import Flask, request, jsonify
import json
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Load user database
with open('user-database.json', 'r') as f:
    user_db = json.load(f)

def check_user_role(username, required_role):
    """Check if a user has the required role."""
    user = user_db.get(username)
    if user and 'roles' in user:
        if required_role in user['roles']:
            return True
    return False

@app.route('/protected', methods=['GET'])
def protected_resource():
    """Example of a protected resource that requires a specific role."""
    auth = request.authorization
    if not auth:
        return jsonify({"status": "failure", "message": "Authentication required"}), 401

    username = auth.username
    if check_user_role(username, 'admin'):
        logging.info(f"User {username} accessed protected resource.")
        return jsonify({"status": "success", "message": "Access granted"}), 200
    else:
        logging.warning(f"User {username} attempted to access protected resource without admin role.")
        return jsonify({"status": "failure", "message": "Unauthorized"}), 403

# Example usage
if __name__ == '__main__':
    app.run(debug=True)
