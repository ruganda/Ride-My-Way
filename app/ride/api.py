from flask.views import MethodView
from flask import jsonify, request, abort, make_response
from app.models import Ride
import uuid
class RideAPI(MethodView):


    def __init__(self):
        
        if request.method != 'GET' and not request.json:
            abort(400)


    def post(self):
        data = request.json
        if not "origin" and  not 'destination' and not 'date' in data :
            abort(400)
        origin = data["origin"]
        destination =data["destination"]
        date = data["date"]
        try:
            res = Ride.offer_ride(origin, destination, date)
            if res == "Ride offered":              
                return jsonify({'msg': res }), 201 
            return jsonify({'msg': res }), 202
        except Exception as e:
            response = {
                'message': str(e)
            }
            return make_response(jsonify(response)), 500

        

        
        

    