from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import random
import string
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app

registered_users = {
    "user1": "./user1",
}
SECRET_KEY = 'your_secret_key_here'


def generate_user_id():
    uid_prefix = 'UI'
    random_numbers = ''.join(random.choices(string.digits, k=5))
    return f"{uid_prefix}{random_numbers}"


@app.route('/sso', methods=['POST'])
def sso():
    # Check if 'userId' is provided in the request
    if 'userId' not in request.form:
        return jsonify({'error': 'Please provide userId'}), 400

    userId = request.form['userId']
    # Check if user is registered
    if userId not in registered_users:
        return jsonify({'error': 'Please register'}), 401
    # Get the uploaded file
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    image_file = request.files['image']
    # Check if file name is empty
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    # Get user's directory
    user_directory = registered_users[userId]
    # Save the image to user's directory
    image_file.save(os.path.join(user_directory, image_file.filename))

    # Generate JWT token with expiration time of 1 week
    # expiration_time = datetime.utcnow() + timedelta(days=7)
    # token_payload = {'userId': userId, 'exp': expiration_time}
    # jwt_token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')
    # print(jwt_token)
    # return jsonify({'message': 'Image uploaded successfully', 'token': jwt_token.decode('utf-8')}), 200
    return jsonify({'message': 'Image uploaded successfully'})


@app.route('/register', methods=['POST'])
def register():
    if 'username' not in request.form or 'password' not in request.form or 'image' not in request.files:
        return jsonify({'error': 'Please provide username, password, and image'}), 400
    username = request.form['username']
    password = request.form['password']
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    userId = generate_user_id()
    user_directory = os.path.join(os.getcwd(), 'users', userId)
    os.makedirs(user_directory, exist_ok=True)
    image_file.save(os.path.join(user_directory, image_file.filename))
    registered_users[userId] = {'username': username,
                                'password': password, 'directory': user_directory}
    response = {
        'userId': userId,
        'image_url': os.path.join(user_directory, image_file.filename)
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
