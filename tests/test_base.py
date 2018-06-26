""" Tests module """
import unittest
from flask import json
from app import create_app

class TestBase(unittest.TestCase):
    """ Base class for all test classes """
    app = create_app('TESTING')
    app.app_context().push()
    client = app.test_client()
