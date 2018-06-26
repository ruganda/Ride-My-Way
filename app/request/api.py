from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from app.models import Ride
import uuid


class RequestAPI(MethodView):
    """This class-based view for requesting a ride."""

    def post(self, ride_id):
        ride_id = uuid.UUID(ride_id)
        try:
            res = Ride.join_ride(ride_id)
            if res == "A request to join this ride has been sent":
                return jsonify({'msg': res}), 201

        except Exception as e:
            response = {
                'message': str(e)
            }
            return make_response(jsonify(response)), 500
