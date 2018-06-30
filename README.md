[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8c610e35181344f08f87fe99b4c65c22)](https://app.codacy.com/app/ruganda/Ride-My-Way?utm_source=github.com&utm_medium=referral&utm_content=ruganda/Ride-My-Way&utm_campaign=badger)
[![Build Status](https://travis-ci.org/ruganda/Ride-My-Way.svg?branch=develop)](https://travis-ci.org/ruganda/Ride-My-Way)
[![Coverage Status](https://coveralls.io/repos/github/ruganda/Ride-My-Way/badge.svg?branch=develop)](https://coveralls.io/github/ruganda/Ride-My-Way?branch=develop)
<a href="https://codeclimate.com/github/ruganda/Ride-My-Way/maintainability"><img src="https://api.codeclimate.com/v1/badges/067eaa497de418427d8b/maintainability" /></a>

# Ride-My-Way
Ride-my App is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers.

# Hosting 
- The api is hosted on heroku https://ruga.herokuapp.com/api/v1/rides/

# Documentation
- https://ridemyway.docs.apiary.io/#reference

# Features
- Get all ride offers
- Get a specific ride offer
- Create a ride offer
- Make a request to join a ride.



# To get started
- clone the repo $ git clone https://github.com/ruganda/Ride-My-Way.git
- $ cd into the project directory
- set up a virtual environment  $ virtualenv venv
- Activate the virtual environment 
- Install project dependencies $ pip install -r requirements.txt
- To run the project $ python run.py
- Open postman and navigate to  http://127.0.0.1:5000/api/v1/rides/



# Create a ride offer
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/Api-v1/screenshots/post.PNG)

# Get all ride offers
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/Api-v1/screenshots/get_all.PNG)

# Get a specific ride offer
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/Api-v1/screenshots/get_one.PNG)

# Make a request to join a ride
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/Api-v1/screenshots/join.PNG)


# Technologies used.
- Python Language
- Flask framework

# Tests
- To run tests $ nosetests
- To run tests with coverage $ nosetests --with-coverage --cover-erase --cover-package=app/ && coverage report

# Purpose of the challenge
- Andela bootcamp challenge 2.