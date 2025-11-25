# This is the main app file where the Flask app is created and configured
# This is where we will initialize our Flask application, set up the database, and define the routes.


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config