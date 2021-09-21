from flask import Blueprint, request
from . import dtos, service

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/sign-up', methods = ['POST'])
def sign_up():
    user, token = service.sign_up(dtos.client_from_json(request.get_json()))
    return dtos.json_from_client(user, token)

@auth.route('/sign-in', methods = ['POST'])
def sign_in():
    user, token = service.sign_in(dtos.client_from_json(request.get_json()))
    return dtos.json_from_client(user, token)