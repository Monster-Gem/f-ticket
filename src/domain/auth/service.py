from jwt import encode
from domain.user import service
from werkzeug.exceptions import Conflict, NotFound
from werkzeug.security import check_password_hash, generate_password_hash
from settings import SECRET_KEY
from datetime import datetime, timedelta

def sign_up(client):
    if service.get_user(client.email):
        raise Conflict('User already exists. Please Log in.')
    else:
        client.password = generate_password_hash(client.password)
        user = service.add_user(client)
        return user, get_token(user).decode('UTF-8')

def sign_in(client):
    user = service.get_user(client.email)
    if user:
        if check_password_hash(user.password, client.password):
            return user, get_token(user).decode('UTF-8')
        else:
            raise NotFound('Could not verify.')
    else:
        raise NotFound('Could not verify.')

def get_token(user):
    return encode({
        'public_id': user.public_id,
        'exp' : datetime.utcnow() + timedelta(minutes = 30)
    }, SECRET_KEY)