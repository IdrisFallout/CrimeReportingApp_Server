from flask import Blueprint, jsonify, request
from DatabaseModule.database import fetch_users, register_user, login_user, hash_to_password, validate_phone_number

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    phone = request.json['phone']
    pin = request.json['pin']
    phone = str(phone)
    if phone.startswith("0"):
        phone = f'+254{phone[1:]}'

    if login_user(phone) is None:
        response = {
            'responseType': 'error',
            'message': 'Invalid phone or pin'
        }
        return jsonify(response), 200

    if not hash_to_password(pin, login_user(phone)):
        response = {
            'responseType': 'error',
            'message': 'Invalid phone or pin'
        }
        return jsonify(response), 200
    response = {
        'responseType': 'success',
        'message': 'Login successful'
    }
    return jsonify(response), 200


@auth.route('/get_users', methods=['GET'])
def get_user():
    response = {
        'responseType': 'success',
        'message': fetch_users()
    }
    return jsonify(response), 200


@auth.route('/signup', methods=['POST'])
def register():
    phone = request.json['phone']
    full_name = request.json['full_name']
    pin = request.json['pin']

    phone = str(phone)
    if not validate_phone_number(phone):
        response = {
            'responseType': 'error',
            'message': 'Validation Failed. Invalid Phone Number'
        }
        return jsonify(response), 200
    if phone.startswith("0"):
        phone = f'+254{phone[1:]}'
    if len(str(pin)) != 4:
        response = {
            'responseType': 'error',
            'message': 'Pin must be 4 digits'
        }
        return jsonify(response), 200
    if not str(pin).isdigit():
        response = {
            'responseType': 'error',
            'message': 'Pin must be a number'
        }
        return jsonify(response), 200
    if register_user(phone, full_name, pin):
        response = {
            'responseType': 'success',
            'message': 'Signup successful'
        }
        return jsonify(response), 200
    else:
        response = {
            'responseType': 'error',
            'message': 'Signup failed'
        }
    return jsonify(response), 200
