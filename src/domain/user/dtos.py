from flask_mongoengine import BaseQuerySet
from werkzeug.security import generate_password_hash

def args_to_email(args):
    return args.get('email', None)

def json_to_update_user(user_json):
    return { 'email': user_json.get('email', None), 'password': generate_password_hash(user_json.get('password', None)) }

def json_from_user(user):
    return {"email": user.email}

def json_from_users(users):
    return {"users": list(map(json_from_user, users))} if isinstance(users, BaseQuerySet) else json_from_user(users)