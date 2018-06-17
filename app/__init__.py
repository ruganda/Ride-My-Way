from flask import Flask, jsonify
from config import configuration

app = Flask(__name__)


# @app.errorhandler(404)
# def handle_errors(e):
#     response = {
#         'status': 'Error',
#         'message': 'The URL you in your request does not exist'
#     }
#     return jsonify(response), 404


def create_app(configuration_name):
    app.config.from_object(configuration[configuration_name])

    from app.ride.views import ride_app
    from app.request.views import request_app
    # register_blueprint
    app.register_blueprint(ride_app)
    app.register_blueprint(request_app)


    return app