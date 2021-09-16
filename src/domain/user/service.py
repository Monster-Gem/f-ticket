from . import repository

def get_users(email=None):
    return get_user(email) if email is not None else repository.get_all_users()

def get_user(email):
    return repository.get_user(email)

def add_user(user):
    return repository.add_user(user)

def delete_user(email):
    repository.delete_user(get_user(email))
    return