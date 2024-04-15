from flask import Flask, request, jsonify , render_template, redirect, url_for
from flask_cors import CORS
import os
import random
import string
import jwt
from datetime import datetime, timedelta
from main import login,register
from emailer import sendEmail
import bcrypt
import pymysql

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your Flask app
#=========================================db 
HOST = 'localhost'
USER = 'root'
PASSWORD = 'Mysqlvarun#2004'
DATABASE = 'RAMCO_TESTDB'

conn = pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DATABASE)
conn.commit()
cursor = conn.cursor()
print(conn)

def get_all_empids():
    try:
        sql = "SELECT empid FROM employees"
        cursor.execute(sql)
        results = cursor.fetchall()
        return [result[0] for result in results]
    except Exception as e:
        print("Error fetching user IDs:", e)
        return []

def is_user_registered(input_empid):
    try:
        empids = get_all_empids()
        if input_empid in empids:
                return True
        return False
    except Exception as e:
        print("Error checking user registration:", e)
        return False

def generate_empid():
    uid_prefix = 'UI'
    random_numbers = ''.join(random.choices(string.digits, k=5))
    return f"{uid_prefix}{random_numbers}"

def register_user(empid):
    os.makedirs(os.path.join(os.getcwd(), empid))


def register_user_db(empid,email):
    try:
        sql = "INSERT INTO employees (empid,email) VALUES (%s, %s)"
        cursor.execute(sql,(empid,email))
        conn.commit()
        register_user(empid)
        return True
    except Exception as e:
        print("Error:", e)
        conn.rollback()
        return False
    
#========================================================
SECRET_KEY = 'your_secret_key_here'

@app.route('/sso', methods=['POST'])
def sso():
    # Check if 'userId' is provided in the request
    try:
        if 'userId' not in request.form:
            return jsonify({'error': 'Please provide userId'}), 400
        userId = request.form['userId']
        if not is_user_registered(userId):
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
    except Exception as e:
            return jsonify({'message': e}) , 401

#=================================================================
@app.route('/ssor', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        empid = generate_empid()
        email = request.form.get('emailid')
        image_file = request.files['image']
        if image_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if register_user_db(empid,email):
            image_path = os.path.join(empid, "original.png")
            image_file.save(image_path)
            register(empid)
            sendEmail("./"+empid+"/share2.png", email,empid)
            return jsonify({'message': 'Registration successful', 'empId': empid}), 200
        else:
            return jsonify({'error': 'User ID already exists'}), 400
    return render_template('register.html')


if __name__ == '__main__':
    app.run(port=4000)
