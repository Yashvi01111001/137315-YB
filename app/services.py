from flask_mail import Message # Importing Message class from Flask-Mail for email handling
import joblib  # Importing joblib for loading machine learning models
import numpy as np  # Importing NumPy for array manipulation
from app import mail # Importing the mail object from the app module
import random # Importing random for generating random strings
import string # Importing string for string manipulation
from app.db_operations import get_latest_soil_parameters_by_user  # Importing a function for database operations

# Function to generate an activation code of a specific length (default length is 6)
def generate_activation_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))



# Function to send an activation email containing an activation code to a specified email address
def send_activation_email(email, activation_code):
    msg = Message('Activate your Smart Farming Account', sender='noreply@smartfarming.com', recipients=[email])
    msg.body = f'Your activation code is: {activation_code}. Use this code to activate your account.'
    mail.send(msg)

# Function to generate an activation code and send it to the specified email address
def send_activation_code_email(email):
    activation_code = generate_activation_code()
    try:
        send_activation_email(email, activation_code)
        return activation_code
    except Exception as e:
        return None
    
# Function to send an email for user account verification, providing an activation code   
def user_verification_email(email, activation_code):
    msg = Message('Activate your Smart Farming Account', sender='noreply@smartfarming.com', recipients=[email])
    msg.body = f' Your tried logging in but you account has not been verfied. \n Kindly activate your account to login. Your activation code is: {activation_code}. Use this code to activate your account.'
    mail.send(msg)
# Function to send a success email upon successful user verification
def user_verification_successfull(email):
    msg = Message('Verification successfull', sender='noreply@smartfarming.com', recipients=[email])
    msg.body = f'Hello ,Welcome to Smart Farming! Your account has been successfully verified. '
    mail.send(msg)

# Loading the machine learning model for crop prediction from the specified path
model = joblib.load('ml_model/smart_farmingmodel.joblib')
def predict_crop_for_user(user_id):
    latest_params = get_latest_soil_parameters_by_user(user_id)

    # Check if soil parameters for the user exist
    if latest_params:
        features = [
                latest_params.nitrogen_level,
                latest_params.phosphorus_level,
                latest_params.potassium_level,
                latest_params.temperature,
                latest_params.humidity,
                latest_params.ph_level,
                latest_params.rainfall
            ]
    # Reshaping features into a NumPy array for prediction
    features_array = np.array(features).reshape(1, -1) 
      # Predicting the crop using the loaded machine learning model
    prediction = model.predict(features_array)
     # Converting prediction to a list if it exists, otherwise return None
    return prediction.tolist() if prediction is not None else None  # Convert prediction to list