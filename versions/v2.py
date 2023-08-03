from flask import Blueprint, jsonify

api_v2 = Blueprint('api_v2', __name__)


@api_v2.route('/resource', methods=['GET'])
def get_resource():
    response = {
        'responseType': 'success',
        'message': 'Version 2 of the resource'
    }
    return jsonify(response), 200