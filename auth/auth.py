from flask import Blueprint, jsonify

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    response = {
        'responseType': 'success',
        'message': 'Login successful'
    }
    return jsonify(response), 200


@auth.route('/signup', methods=['POST'])
def signup():
    response = {
        'responseType': 'success',
        'message': 'Signup successful'
    }
    return jsonify(response), 200
