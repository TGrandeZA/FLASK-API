# Importing the Flask app and database instance from the api module
from api import app, db 

#Creating the database, allows access the database and configuration settings from the 'app' object.
with app.app_context(): 

    # Creating all database tables defined by the SQLAlchemy models (UserModel Class)
    db.create_all()  