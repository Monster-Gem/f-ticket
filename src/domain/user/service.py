from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_users(email=None):
    return get_user(email) if email is not None else repository.get_all_users()

def get_user_by_public_id(public_id):
    return repository.get_user_by_public_id(public_id)

def get_user(email):
    user = repository.get_user(email)
    if not user:
        raise NotFound('User does not exists.')
    else:
        return user

def add_user(user):
    try:
        get_user(user.email)
        raise Conflict('User already exists. Please Log in.')
    except NotFound:
        return repository.add_user(user)

def delete_user(email):
    repository.delete_user(get_user(email))
    return

def update_user(email, update_user):
    return repository.update_user(get_user(email), update_user)

def set_user_token(user, token):
    return repository.set_user_token(user, token)

def reset_user_token(user):
    return repository.set_user_token(user, None)
