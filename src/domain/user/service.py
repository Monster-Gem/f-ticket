from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_users(email=None):
    return get_user(email) if email is not None else repository.get_all_users()

def get_user_by_public_id(public_id):
    return repository.get_user_by_public_id(public_id)

def get_user(email):
    return repository.get_user(email)

def add_user(user):
    if get_user(user.email):
        raise Conflict('User already exists. Please Log in.')
    else:
        return repository.add_user(user)

def delete_user(email):
    repository.delete_user(get_user(email))
    return

def update_user(email, update_user):
    user = get_user(email)
    if not user:
        raise NotFound('User does not exists.')
    else:
        return repository.update_user(user, update_user)