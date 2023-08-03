from flask import Flask, jsonify
from versions import v1, v2
from auth.auth import auth as auth_blueprint

app = Flask(__name__)

app.register_blueprint(v1.api_v1, url_prefix='/api/v1')
app.register_blueprint(v2.api_v2, url_prefix='/api/v2')
app.register_blueprint(auth_blueprint, url_prefix='/auth')


@app.errorhandler(404)
def not_found_error(error):
    response = {
        'responseType': 'error',
        'message': f'{error}'
    }
    return jsonify(response), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    response = {
        'responseType': 'error',
        'message': f'{error}'
    }
    return jsonify(response), 405


# handle error 400 bad request
@app.errorhandler(400)
def bad_request_error(error):
    response = {
        'responseType': 'error',
        'message': f'{error}'
    }
    return jsonify(response), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
