# Django Movie Database
This is a Django Rest Framework project for a movie database. The project consists of two apps:
1. Users: This app contains the User model and APIs for user registration and login.
2. Movies and Cast: This app contains the Movie and Cast models and APIs for creating, retrieving and listing movies and cast members.

## User Model
The User model has the following fields:
- id: integer
- username: string
- email: string
- password: string
- created_at: datetime (ISO 8601 format)
- updated_at: datetime (ISO 8601 format)

## APIs
### Users
- Register a user: API to register the user details including name, email, password, and confirm password.
- Login user: API to log in a user using JWT Authentication with username and password.

### Movies and Cast
- List all movies: API to retrieve a list of all movies in the system.
- Retrieve a movie: API to retrieve a specified movie by id.
- Create a movie: API to create a new movie and return the new object.
- Create a cast member: API to create a cast member and return the new object.

## Extension to TV Shows
If the database is to be extended to incorporate TV shows, a new model named "TV Show" can be created with the required fields. The necessary serializers, views, and URLs can also be added to support the TV Show model.

OR

We can use proxy model to add new functionality to existing model.

## Deployment
Clone this repository and run the following commands in the project directory to deploy the application:

    pip install -r requirements.txt
    python manage.py makemigration users
    python manage.py migrate users
    python manage.py migrate
    python manage.py runserver

