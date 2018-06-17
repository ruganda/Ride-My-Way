from flask import Blueprint

from app.ride.api import RideAPI

ride_app = Blueprint('ride_app', __name__)

ride_view = RideAPI.as_view('ride_api')
ride_app.add_url_rule('/api/v1/rides/', defaults={'ride_id': None},
                 view_func=ride_view, methods=['GET',])
ride_app.add_url_rule('/api/v1/rides/', view_func=ride_view, methods=['POST',])
ride_app.add_url_rule('/api/v1/rides/<ride_id>', view_func=ride_view,
                 methods=['GET',])

