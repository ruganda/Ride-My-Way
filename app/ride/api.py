"""This module handles RideAPI class and its methods"""
import uuid
from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from app.models import Ride


class RideAPI(MethodView):
    """This class based view handles ride related methods"""

    def get(self, ride_id):
        """Method for  get requests"""
        if ride_id:
            ride_id = uuid.UUID(ride_id)
            rides = Ride.view_all_rides()
            for ride in rides:
                if ride_id == ride['Id']:
                    return jsonify(ride), 200
                return jsonify({'msg': "Ride not found "}), 404
        else:
            rides = Ride.view_all_rides()
            if rides == []:
                response = {
                    "msg": " There are no rides rides at the moment"}
                return make_response(jsonify(response)), 200
            return jsonify(rides), 200

    def post(self):
        '''Method for a post request'''
        data = request.json
        origin = data["origin"]
        destination = data["destination"]
        date = data["date"]
        res = Ride.offer_ride(origin, destination, date)
        if res == "Ride offered":
            return jsonify({'msg': res}), 201
        return jsonify({'msg': res}), 409
