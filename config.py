import os
from flask import Flask
from dotenv import load_dotenv
from flask_mail import Mail

# Creating a Flask application instance
app = Flask(__name__)

# Loading environment variables from the .env file 
load_dotenv()  


# Defining a configuration class for application settings
class Config:
    # Configuring SQLAlchemy database URI from environment variables
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    
   # Configuration for Flask-Mail
    MAIL_SERVER = os.getenv('MAIL_SERVER')  # Mail server details
    MAIL_PORT = int(os.getenv('MAIL_PORT'))  # Mail server port (converted to integer)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Mail username
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # Mail password
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS').lower() == 'true'  # Using TLS for email (boolean)
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL').lower() == 'true'  # Using SSL for email (boolean)

 
