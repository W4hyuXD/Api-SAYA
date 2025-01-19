from flask import Flask, jsonify, request

app = Flask(__name__)

# Data dummy
data = [
    {"id": 1, "name": "Wahyu"},
    {"id": 2, "name": "Evi"}
]

# Endpoint GET
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data), 200

# Endpoint GET by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((item for item in data if item["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# Endpoint POST
@app.route('/api/users', methods=['POST'])
def add_user():
    new_user = request.json
    data.append(new_user)
    return jsonify(new_user), 201

# Endpoint PUT
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((item for item in data if item["id"] == user_id), None)
    if user:
        updated_data = request.json
        user.update(updated_data)
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

# Endpoint DELETE
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global data
    data = [item for item in data if item["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
