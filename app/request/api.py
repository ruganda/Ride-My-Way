"""This module handles the class RequestApi and its post method"""
import uuid
from flask.views import MethodView
from flask import jsonify
from app.models import Ride


class RequestAPI(MethodView):
    """This class-based view for requesting a ride."""

    def post(self, ride_id):
        '''sends a request to join a ride'''
        ride_id = uuid.UUID(ride_id)
        res = Ride.join_ride(ride_id)
        if res == "A request to join this ride has been sent":
            return jsonify({'msg': res}), 201
