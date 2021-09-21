from domain.user import entity
from werkzeug.exceptions import Unauthorized

def json_from_client(user, token):
    return {"email": user.email, "token": token}

def client_from_json(user_json):
    email = user_json.get('email')
    password = user_json.get('password')
    if not email or not password:
        raise Unauthorized('Email or password not found')
    else: 
        return entity.User(email=email, password=password)