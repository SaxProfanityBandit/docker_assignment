# Docker Assignment

This is a simple project for my DevOps education that touches upon Docker, docker-compose, MySQL and Flask.

## Instructions
Clone the project and make sure you have terminal in the main project folder, make sure you got docker and docker-compose installed. 
When you want to start it up you run 
```
docker compose up. 
```
You can then enter visit the flask site by localhost:5000. It has one route called /users and has support for GET and POST, the GET lists all users in the database, POST supports receiving json to make a new user.

To make a new user, use POST to send json formated like this:
```
{"name":"Sax","age":28}
```

Make an issue should any problems should arrive.
