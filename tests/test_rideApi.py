from test_base import TestBase
import unittest
from flask import json
from test_data import*


class TestRide(TestBase):
    """ Defines tests for the view methods of for rides """

    def setUp(self):
        pass

    
    
    def test_ride_creation(self):
        """Test API can create a ride (POST request)"""
        
        response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(post_ride1))

        self.assertEqual(response.status_code, 201)
        self.assertIn('Ride offered', str(response.data))
    
    def test_ride_creation_with_invalid_date_fomart(self):
        """Test if a ride can be created on an invalid date formart"""
        
        response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(invalid_date))

        self.assertIn('does not match format', str(response.data))
    
    def test_ride_creation_given_past_date(self):
        """Test if a ride can be created with a past date"""
 
        response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(past_date))

        self.assertIn("rides can only have a future date", str(response.data))

    def test_duplicate_ride_creation(self):
        """Test if an api allows duplicate rides"""
        self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(duplicate_ride))
        response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(duplicate_ride))

        self.assertIn("ride already exists", str(response.data))



    def test_api_can_view_all_rides(self):
        """Test RideAPI can view all (GET request)."""

        response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(post_ride2))

        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("destination", str(response.data))
      

    
    def test_api_can_get_ride_by_id(self):
        """Test API can fetch a single ride by using it's id."""
        # post data
        response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(post_ride3))

        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        
        results = json.loads(response.data.decode())
        

        for ride in results:
            result = self.client.get(
                'api/v1/rides/{}'.format(ride['Id']))
            self.assertEqual(result.status_code, 200)
            self.assertIn(ride['Id'], str(result.data))

    def test_join_request_issuccesful(self):
        """Test API can succesfully send a request to join a ride (POST request)"""
        response = self.client.post('api/v1/rides/',
                                      content_type='application/json',
                                      data=json.dumps(post_ride4))

        self.assertEqual(response.status_code, 201)
        response = self.client.get('api/v1/rides/')
        self.assertEqual(response.status_code, 200)
        
        results = json.loads(response.data.decode())
    

        for ride in results:
            
            response = self.client.post('api/v1/rides/{}/requests'.format(ride['Id']),
                                        content_type='application/json',
                                        data=json.dumps({'join':'True'}))
            self.assertEqual(response.status_code, 201)
            self.assertIn("A request to join this ride has been sent", str(response.data))
    
