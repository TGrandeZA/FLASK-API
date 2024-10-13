# 📊 Flask User Management API

Welcome to the **Flask User Management API**! This is a RESTful API I built with Flask and SQLAlchemy to manage user data, including creating, retrieving, updating, and deleting user records.

## 🤔 What is an API?

**API** stands for **Application Programming Interface**. In simple terms, an API is a set of rules and protocols that allows different software applications to communicate with each other. Think of it as a waiter in a restaurant who takes your order (request) and brings you the food (response) from the kitchen (server).

### 🛠 How APIs Work

1. **Request**: A client (like a web browser or a mobile app) sends a request to the server through the API.
2. **Processing**: The server processes the request, performs the necessary actions (like accessing a database), and prepares the response.
3. **Response**: The server sends back the response to the client through the API.

### 📈 Relevance in Data Analytics

APIs play a crucial role in data analytics by enabling the seamless flow of data between different systems and platforms. Here's how:

- **Data Collection**: APIs allow analysts to gather data from various sources such as social media platforms, financial markets, and web services without manual intervention.
- **Real-Time Data Access**: With APIs, analysts can access real-time data, which is essential for making timely and informed decisions.
- **Integration with Analytical Tools**: APIs enable the integration of data with analytical tools and dashboards, facilitating advanced data analysis and visualization.

### ⚙️ Relevance in Data Engineering

In data engineering, APIs are fundamental for building and maintaining robust data pipelines. Here's why:

- **Data Integration**: APIs allow data engineers to connect different data sources, ensuring that data flows smoothly between systems like databases, data warehouses, and cloud services.
- **Automation**: APIs enable the automation of data workflows, reducing the need for manual data handling and minimizing errors.
- **Scalability**: With APIs, data pipelines can be easily scaled to handle large volumes of data, ensuring that data processing remains efficient as the organization grows.
- **Interoperability**: APIs ensure that different systems and applications can work together seamlessly, enhancing the overall architecture of data infrastructure.

### 📝 Example in Our Project

In our **Flask User Management API** project, the API allows clients to:

- **Create** new users by sending `POST` requests.
- **Retrieve** user information with `GET` requests.
- **Update** user details using `PATCH` requests.
- **Delete** users through `DELETE` requests.

This API facilitates the management of user data, making it easy to integrate with other applications, perform data analysis on user information, and build scalable data-driven features.


## 🧠 Skills Acquired

During the development of this project, I gained valuable skills, including:

- **Flask**: Understanding how to build web applications using the Flask framework.
- **SQLAlchemy**: Learning how to interact with databases through SQLAlchemy for object-relational mapping (ORM).
- **RESTful API Development**: Gaining experience in designing and implementing RESTful APIs for user management.
- **Error Handling**: Implementing proper error handling and debugging techniques in a web application.
- **Database Management**: Managing SQLite databases and querying data effectively.
- **HTTP Protocols**: Understanding how to use HTTP methods (GET, POST, PATCH, DELETE) to handle requests and responses in a web application.



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
    











