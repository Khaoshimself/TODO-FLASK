# TODO Flask Application

## Introduction
This Flask application is a simple yet functional Todo list manager. It allows users to add tasks to a list and stores them in a SQLite database. The application is built using Flask, a micro web framework for Python, and utilizes Flask-WTF for form handling and Flask-SQLAlchemy for database interactions.

## Prerequisites
Before you begin, ensure you have met the following requirements:

- Python 3.x
- Flask
- Flask-WTF
- Flask-SQLAlchemy

## Installation
To install the TODO Flask Application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Khaoshimself/TODO-FLASK.git
Navigate to the project directory:

bash
Copy code
cd your-repository
Install the required packages:

bash
Copy code
pip install Flask Flask-WTF Flask-SQLAlchemy
Running the Application
To run the TODO Flask Application, use the following command:

bash
Copy code
flask run
This will start a development server, and the application will be accessible at http://127.0.0.1:5000/.

Application Functionality
Add Todo: Users can add new tasks to the todo list via a simple form. Each task is stored in the SQLite database.
View Todos: The homepage displays all the tasks added by the user, retrieved from the database.
