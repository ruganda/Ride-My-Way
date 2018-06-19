from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from app.models import Ride

import uuid


class RideAPI(MethodView):

    def __init__(self):

        if request.method != 'GET' and not request.json:
            abort(400)

    def get(self, ride_id):
        """Method for  get requests"""
        if ride_id:
            try:
                ride_id = uuid.UUID(ride_id)
                rides = Ride.view_all_rides()
                for ride in rides:
                    if ride_id == ride['Id']:
                        return jsonify(ride), 200
                    return jsonify({'msg': "Ride not found "}), 404
            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 500

        else:
            try:
                rides = Ride.view_all_rides()
                if rides == []:
                    return jsonify({"msg": " There are no rides rides at the moment"}), 200
                return jsonify(rides), 200
            except Exception as e:
                response = {
                    'message': str(e)
                }
                return make_response(jsonify(response)), 500

    def post(self):
        '''Method for a post request'''
        data = request.json
        if not "origin" and not 'destination' and not 'date' in data:
            abort(400)
        origin = data["origin"]
        destination = data["destination"]
        date = data["date"]
        try:
            res = Ride.offer_ride(origin, destination, date)
            if res == "Ride offered":
                return jsonify({'msg': res}), 201
            return jsonify({'msg': res}), 409
        except Exception as e:
            response = {
                'message': str(e)
            }
            return make_response(jsonify(response)), 500
