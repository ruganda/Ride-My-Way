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



    