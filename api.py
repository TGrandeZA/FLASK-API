from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

# Initialising a Flask application
app = Flask(__name__)

# SQLite Databse initialisation
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app) 

# Defining the structure of the User table in the database
class UserModel(db.Model): 
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique= True, nullable=False)
    email = db.Column(db.String(80), unique = True, nullable=False)

    # String representation of the user object
    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"
    



# Setting up error handling for HTTP requests with a parser 
user_args = reqparse.RequestParser()
user_args.add_argument('name',  type=str, required = True, help= "Name cannot be blank")
user_args.add_argument('email',  type=str, required = True, help= "Email cannot be blank")


# Defining the fields to be returned in JSON (using a dictionary-Key, value pairing), for easy machine parsing
userFields = {
    'id': fields.Integer,
    'name':fields.String, 
    'email':fields.String,
}


# Defining a resource for managing multiple users (HTTP requests)
class Users(Resource):
    @marshal_with(userFields) #Decorator, automatically format the output using userFields (JSON Format)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userFields)
    def post(self): 
        args = user_args.parse_args()
        user = UserModel(name = args["name"], email = args["email"])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201  #Succesful request = 200, Created = 201
    

    
    
#Defining a resource for managing a specific user (HTTP Requests)
class User(Resource):

    # HTTP GET request to fetch a user by their ID
    @marshal_with(userFields)  
    def get(self, id): 
        try:
            user = UserModel.query.filter_by(id=id).first() # Find the user with the specified ID
            if not user:
                abort(404, "User not found") #404 = Not found 
            return user
        except Exception as e:
            print(f"Error occurred: {e}")
            abort(500, "An internal error occurred.")

    
    # HTTP PATCH request to update a user by their ID
    @marshal_with(userFields)
    def patch(self, id):
        try:
            args = user_args.parse_args() #parse incoming JSON data
            user = UserModel.query.filter_by(id=id).first()
            if not user:
                abort(404, "User not found") #404 = Not found 
            user.name = args["name"]
            user.email = args["email"]
            db.session.commit() #commit the changes to the database 
            return user
        
        except Exception as e:
            print(f"Error occurred: {e}")
            abort(500, "An internal error occurred.")

    
    #HTTP request to delete a particular user if they are found using their ID
    @marshal_with(userFields)
    def delete(self, id):
        try: 
            user = UserModel.query.filter_by(id=id).first()
            if not user:
                abort(404, "User not found") #404 = Not found 
            db.session.delete(user)
            db.session.commit() #commit the changes to the databse 
            users = UserModel.query.all()
            return user, 200 #200 = confirms succesful deletion for a particular user
        
        except Exception as e:
            print(f"Error occurred: {e}")
            abort(500, "An internal error occurred.")


# Setting up the API resources and their corresponding endpoints
api.add_resource(Users, '/api/users/') # Route for managing multiple users
api.add_resource(User, '/api/users/<int:id>') # Route for managing a specific user by ID

# Defining a simple homepage for the application
@app.route('/')
def home(): 
    return '<h1>Flask REST API </h1>'

# Starting the Flask application
if __name__ == '__main__': 
    app.run(debug = False)

