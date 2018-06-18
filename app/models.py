import uuid
from datetime import date, datetime

rides = []
requests = []

class Ride(object):
    ''' A Rides class'''

    def __init__(self, ride_id, origin, destination, date, join = "False"):
        ''' Initializes the ride object'''
        self.ride_id = ride_id
        self.origin = origin
        self.destination = destination
        self.date = date
        self.join = join
        

    @classmethod
    def existing_ride(cls, origin, destination, date):
        """A method to check if the same ride already exists """
        for ride in rides:
            if ride['origin'] == origin and ride['destination'] == destination and ride['date'] == date:
                return True
        else:
            return False

    @classmethod
    def valid_date(cls, date):
        """Check if the given date is less than the current date"""
        date = datetime.strptime(date, '%Y-%m-%d').date()
        if date <= date.today():
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
                cls.data["join"] = "False"

                rides.append(cls.data)
                return "Ride offered"

    @classmethod
    def view_all_rides(cls):
        """ Return all the rides"""
        return rides

    @classmethod
    def join_ride(cls, ride_id):
        for ride in rides:
            if ride['Id'] == ride_id:
                ride['join'] == "True"
                requests.append(ride)
                return "A request to join this ride has been sent"

        


