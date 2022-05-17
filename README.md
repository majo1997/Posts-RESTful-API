Simple RESTful API providing endpoints for post management.
API is built in python using flask-restful and sqlite database with SQLAlchemy.

How to run 

docker build -t flask-rest-api .

docker run flask-rest-api

docker run -d -p 5000:5000 flask-rest-api

#docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}'