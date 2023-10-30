import re
from string import punctuation, ascii_lowercase, ascii_uppercase, digits
from datetime import datetime, timedelta

from wtforms.validators import ValidationError
from app.models import User


# Validation functions for forms.py

# Passowrd validation criteria dictionary
required_chars = {"upper": ascii_uppercase, "lower": ascii_lowercase, "digits": digits, "symbols": punctuation}

def validate_password_chars(form, field):
    '''
    Validates if password contains at least 1 character from each criteria that are provided in
    required_chars dictionary.
    
    if all conditions are met, the is_four variable will have the value 4 and the password passes
    the validation, if a condition is missing, is_four variable will have a value which is less than
    4 and a validation error will be raised.
    '''
    is_four = 0
    for rule in required_chars:
        for char in required_chars[rule]:
            if char in field.data:
                is_four += 1
                break
    
    if is_four < 4:
        raise ValidationError("Password does not meet requirements")
    
def validate_username(form, field):
    '''
    Validates if username meets criteria (length is between 3 and 16 characters,
    only includes letters, numbers, underscore and hyphen) and ensure that the
    username does not exist in database, else, it raises validation error.
    '''
    
    if re.match(r"^[a-zA-Z0-9_-]{3,16}$", field.data):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError("Username already exists")        
    else:
        raise ValidationError("Invalid username")        
    

def validate_email(form, field):
    '''
    Validates that email does not exist in database, else, it raises validation error.
    '''
    user = User.query.filter_by(email=field.data).first()
    if user:
        raise ValidationError("Email already exists")
        
def validate_extension(form, field):
    '''
    Validates that the file that was provided contains one of the allowed extensions, else,
    it raises validation error.
    '''
    allowed_extensions = ["png", "jpg", "jpeg", "gif"]
    
    if field.data.filename:
        ext = field.data.filename.split(".")[1]
        if ext not in allowed_extensions:
            raise ValidationError("File type not allowed")
        
# Datetime formatting class for routes.py
    
class DateTimeFormat:
    '''
    A class that takes a datetime object and it includes methods for
    formatting date and time.
    
    date_format method:
        - returns one of the following:
            If the date is today, it returns "Today".
            If the date is yesterday, it returns "Yesterday".
            Otherwise, it returns formatted date.
    time_format method:
        - return formatted time.
    '''
    def __init__(self, date_time: datetime):
        self.date_time = date_time
        
    def date_format(self):
        if self.date_time.date() == datetime.today().date():
            return "Today"
        elif self.date_time.date() == (datetime.today().date() - timedelta(days=1)):
            return "Yesterday"
        else:
            return self.date_time.strftime("%b %d, %Y")
        
    def time_format(self):
        no_zero_hour = self.date_time.strftime("%I") if self.date_time.strftime("%I")[0] != '0' else self.date_time.strftime("%I")[1]
        return self.date_time.strftime(f"{no_zero_hour}:%M %p")
        