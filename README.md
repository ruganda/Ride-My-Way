# Ride-My-Way
Ride-my App is a carpooling application that provides drivers with the ability to create ride offers and passengers to join available ride offers.

# Features
- Get all ride offers
- Get a specific ride offer
- Create a ride offer
- Make a request to join a ride.



# To get staarted
- clone the repo $ git clone https://github.com/ruganda/Ride-My-Way.git
- $ cd into the project directory
- set up a virtual environment  $ virtualenv venv
- Activate the virtual environment 
- Install project dependencies $ pip install -r requirements.txt
- To run the project $ python run.py
- Open postman and navigate to  http://127.0.0.1:5000/api/v1/rides/



# Create a ride offer
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/screenshots/post.PNG)

# Get all ride offers
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/screenshots/get_all.PNG)

# Get a specific ride offer
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/screenshots/get_one.PNG)

# Make a request to join a ride
![alt text](https://raw.githubusercontent.com/ruganda/Ride-My-Way/screenshots/join.PNG)


# Technologies used.
- Python Language
- Flask framework

# Tests
- To run tests $ nosetests
- To run tests with coverage $ nosetests --with-coverage --cover-erase --cover-package=app/ && coverage report

# Authors
 - RUGANDA MUBARAK
# purpose 
- Andela bootcamp challenge 2