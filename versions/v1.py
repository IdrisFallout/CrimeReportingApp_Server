from flask import Blueprint, jsonify

api_v1 = Blueprint('api_v1', __name__)


@api_v1.route('/resource', methods=['GET'])
def get_resource():
    response = {
        'responseType': 'success',
        'message': 'Version 1 of the resource'
    }
    return jsonify(response), 200
