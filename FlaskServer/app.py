from flask import Flask, request, jsonify , render_template, redirect, url_for
from flask_cors import CORS
import os
import random
import string
import jwt
from datetime import datetime, timedelta
from main import login,register


app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app

registered_users = {
    "user1": "user1",
}
SECRET_KEY = 'your_secret_key_here'

def authenticate_admin(username, password):
    # Dummy authentication, replace with your actual logic
    return username == 'admin' and password == 'password'


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
    if userId not in registered_users:
        return jsonify({'error': 'Please register'}), 401
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    image_path = os.path.join(os.getcwd(),userId, "share2.png")
    image_file.save(image_path)
    if(login(userId)):
        return jsonify({'message': 'Successful Signin'}),200
    else :
        return jsonify({'message': 'Invalid Credentials'})
    
import base64
@app.route('/ssor', methods=['POST'])
def ssor():
    if 'userId' not in request.form:
        return jsonify({'error': 'Please provide userId'}), 400

    userId = request.form['userId']
    if userId in registered_users:
        return jsonify({'error': 'Already register'}), 400

    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    userId = generate_user_id()
    user_directory = os.path.join(os.getcwd(), 'users', userId)
    os.makedirs(user_directory, exist_ok=True)
    image_path = os.path.join(user_directory, "original.png")
    image_file.save(image_path)
    registered_users[userId] = {'userId': userId}

    with open(image_path, "rb") as f:
        image_data = f.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')

    response = {
        'userId': userId,
        'image_data': encoded_image
    }

    return jsonify(response), 200

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_admin(username, password):
            response = redirect(url_for('ssorpage'))
            response.set_cookie('admin_authenticated', 'true')
            return response
        else:
            return render_template('admin_login.html', error='Invalid credentials')
    return render_template('admin_login.html', error=None)

#SSO REG PAGE WHERE ADMIN LOGS IN AND CREATES USER SHARES NEED TO BE MADE

#FIX LOGIN ISSUE WITH INVALID CREDENTAILS

#UI FOR PAGE


if __name__ == '__main__':
    app.run(debug=True)
