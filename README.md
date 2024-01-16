# Flask-RESTful POS Application

This is a simple Point of Sale (POS) application built with Flask-RESTful, Flask-Migrate, and SQLite. The application allows you to manage products, perform CRUD operations, and retrieve information using a RESTful API.

# Installation
Clone the repository:


# Copy code
git clone https://github.com/your-username/flask-pos-app.git

# Change into the project directory:
cd flask-pos-app

# Create a virtual environment 
python -m venv venv
Activate the virtual environment:

# On Windows:
.\venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install the dependencies:
pip install -r requirements.txt

# Set up the database:
flask db init
flask db migrate
flask db upgrade

# Run the Flask application:
flask run


