from flask import Flask, jsonify
from config import configuration

app = Flask(__name__)





def create_app(configuration_name):
    app.config.from_object(configuration[configuration_name])

    from app.ride.views import ride_app
    from app.request.views import request_app
    # register_blueprint
    app.register_blueprint(ride_app)
    app.register_blueprint(request_app)


    return app