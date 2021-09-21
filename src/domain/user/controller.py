from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import admin_required
import json

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('', methods = ['GET'])
@admin_required
def get_users(authenticated_user):
    return dtos.json_from_users(service.get_users(dtos.args_to_email(request.args)))

@user.route('', methods = ['DELETE'])
@admin_required
def delete_user(authenticated_user):
    service.delete_user(dtos.args_to_email(request.args))
    return {}

@user.route('', methods = ['PATCH'])
@admin_required
def update_user(authenticated_user):
    return dtos.json_from_users(service.update_user(dtos.args_to_email(request.args), dtos.json_to_update_user(json.loads(request.get_data().decode()))))