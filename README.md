# 📊 Flask User Management API

Welcome to the **Flask User Management API**! This is a RESTful API I built with Flask and SQLAlchemy to manage user data, including creating, retrieving, updating, and deleting user records.

## 📦 Requirements

To run this project, you need the following packages:

- Flask
- Flask-SQLAlchemy
- Flask-RESTful

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```
## 🛠 Installation

  1) Clone the Repository:
     ```bash
     git clone <your-repo-url>
     cd <your-repo-directory>
     ```
  2) Set Up the Database: Ensure you have SQLite installed. Then, run the following command to create the database:
     ```bash
     python create_database.py

  3) Run the Application: Start the Flask application with:
     ```bash
     ./run.sh
     ```
     The application will be running at http://127.0.0.1:5000.

## 🎯 API Endpoints

**Get All Users**
  - Endpoint: /api/users/
  - Method: GET
  - Description: Retrieves a list of all users.

**Get User by ID**
  - Endpoint: /api/users/<int:id>
  - Method: GET
  - Description: Retrieves a user by their ID.

**Create a New User**
  - Endpoint: /api/users/
  - Method: POST
  - Description: Creates a new user. Requires name and email in the request body.

**Update a User**
  - Endpoint: /api/users/<int:id>
  - Method: PATCH
  - Description: Updates the details of a user by their ID. Requires name and email in the request body.

**Delete a User**
  - Endpoint: /api/users/<int:id>
  - Method: DELETE
  - Description: Deletes a user by their ID.

## 🔍 Viewing the Database
To view the database, you can use SQL Browser. Open SQL Browser and load the database.db file to inspect user records and data structure.

## 🎉 Usage
Once the server is running, you can use tools like Postman or Thunderbolt to interact with the API. Simply send requests to the specified endpoints to manage users.

**Example Request**
  - To create a new user, send a POST request to /api/users/ with a JSON body like this:
    ```bash
    {
    "name": "John Doe",
    "email": "john.doe@example.com"
    }
    ```
## ⚙️ License
This project is licensed under the MIT License.










