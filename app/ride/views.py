"""This module register the RIDE_APP Blue_print and adds url rules"""
from flask import Blueprint
from app.ride.api import RideAPI

RIDE_APP = Blueprint('RIDE_APP', __name__)

RIDE_VIEW = RideAPI.as_view('ride_api')
RIDE_APP.add_url_rule('/api/v1/rides/', defaults={'ride_id': None},
                      view_func=RIDE_VIEW, methods=['GET', ])
RIDE_APP.add_url_rule(
    '/api/v1/rides/', view_func=RIDE_VIEW, methods=['POST', ])
RIDE_APP.add_url_rule('/api/v1/rides/<ride_id>', view_func=RIDE_VIEW,
                      methods=['GET', ])
