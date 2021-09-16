from flask_mongoengine import BaseQuerySet
from . import entity

def args_to_email(args):
    return args.get('email', None)

def json_from_user(user):
    return {"email": user.email}

def json_from_users(users):
    return {"users": list(map(json_from_user, users))} if isinstance(users, BaseQuerySet) else json_from_user(users)

def user_from_json(user_json):
    return entity.User(email=user_json.get('email'), password=user_json.get('password'))