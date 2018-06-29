"""This module contains classes Ride and its method"""
import uuid
from datetime import datetime

RIDES = []
REQUESTS = []


class Ride(object):
    ''' A Rides class'''

    def __init__(self, ride_id, origin, destination, ride_date):
        ''' Initializes the ride object'''
        self.ride_id = ride_id
        self.origin = origin
        self.destination = destination
        self.ride_date = ride_date

    @classmethod
    def existing_ride(cls, origin, destination, date):
        """A method to check if the same ride already exists """
        for ride in RIDES:
            if ride['origin'] == origin and ride['destination'] == \
                    destination and ride['date'] == date:
                return True
        return False

    @classmethod
    def valid_date(cls, ride_date):
        """Check if the given date is less than the current date"""
        try:
            ride_date = datetime.strptime(ride_date, '%Y-%m-%d').date()
        except ValueError:
            return "incorrect date format, should be YYYY-MM-DD"
        if ride_date <= ride_date.today():
            return False
        return True

    @classmethod
    def offer_ride(cls, origin, destination, date):
        """A method for offering a ride"""
        cls.data = {}
        if cls.existing_ride(origin, destination, date):
            return "ride already exists"
        else:
            if not cls.valid_date(date):
                return "rides can only have a future date"
            else:
                cls.data['Id'] = uuid.uuid1()
                cls.data['origin'] = origin
                cls.data['destination'] = destination
                cls.data["date"] = date
                RIDES.append(cls.data)
                return "Ride offered"

    @classmethod
    def view_all_rides(cls):
        """ Return all the rides"""
        return RIDES

    @classmethod
    def join_ride(cls, ride_id):
        '''A method for sending a request to join a ride'''
        for ride in RIDES:
            if ride['Id'] == ride_id:
                REQUESTS.append(ride)
                return "A request to join this ride has been sent"
