Simple RESTful API providing endpoints for post management.
API is built in python using flask-restful and sqlite database with SQLAlchemy.

How to run (make sure you created .env file next to .env.example before with appropriate configuration):

docker build -t flask-rest-api .

docker run -d -p 5000:5000 flask-rest-api
