from flask import Blueprint, request
from . import dtos, service, entity

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('', methods = ['GET'])
def get_users():
    return dtos.json_from_users(service.get_users(dtos.args_to_email(request.args)))

@user.route('', methods = ['POST'])
def add_user():
    return dtos.json_from_user(service.add_user(dtos.user_from_json(request.get_json())))

@user.route('', methods = ['DELETE'])
def delete_user():
    service.delete_user(dtos.args_to_email(request.args))
    return {}