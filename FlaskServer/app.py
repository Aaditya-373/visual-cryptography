from flask import Flask, request, jsonify , render_template, redirect, url_for
from flask_cors import CORS
import os
import random
import string
import jwt
from datetime import datetime, timedelta
from main import login,register
from emailer import sendEmail

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app

registered_users = {
    "user1": "user1",
}

SECRET_KEY = 'your_secret_key_here'

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
        os.remove(image_path)
        return jsonify({'message': 'Successful Signin'}),200
    else :
        os.remove(image_path)
        return jsonify({'message': 'Invalid Credentials'}) , 400
    

def register_user(user_id):
    if user_id not in registered_users:
        registered_users[user_id] = user_id
        os.makedirs(os.path.join(os.getcwd(), user_id))
        return True
    return False
# ================================================================
def generate_user_id():
    uid_prefix = 'UI'
    random_numbers = ''.join(random.choices(string.digits, k=5))
    return f"{uid_prefix}{random_numbers}"

def register_user(user_id):
    if user_id not in registered_users:
        registered_users[user_id] = user_id
        os.makedirs(os.path.join(os.getcwd(), user_id))
        return True
    return False

@app.route('/ssor', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        user_id = generate_user_id()
        email = request.form.get('emailid')
        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if register_user(user_id):
            image_path = os.path.join(user_id, "original.png")
            image_file.save(image_path)
            register(user_id)
            sendEmail("./"+user_id+"/share2.png", email,user_id)
            return jsonify({'message': 'Registration successful', 'userId': user_id}), 200
        else:
            return jsonify({'error': 'User ID already exists'}), 400
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
