 
from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import admin_required, user_required
import json

route = Blueprint('route', __name__, url_prefix='/routes')

@route.route('', methods = ['POST'])
@admin_required
def add_route(authenticated_user):
    return dtos.json_from_route(
        service.add_route(
            dtos.route_from_json(request.get_json())))

@route.route('', methods = ['GET'])
@user_required
def get_routes(authenticated_user):
    return dtos.json_from_routes(
        service.get_routes(
            dtos.args_to_origin(request.args), 
            dtos.args_to_destination(request.args)))

@route.route('', methods = ['DELETE'])
@admin_required
def delete_route(authenticated_user):
    service.delete_route(
        dtos.args_to_origin(request.args), 
        dtos.args_to_destination(request.args))
    return {}

@route.route('', methods = ['PATCH'])
@admin_required
def update_route(authenticated_user):
    return dtos.json_from_routes(
        service.update_route(
            dtos.args_to_origin(request.args), 
            dtos.args_to_destination(request.args), 
            dtos.json_to_update_route(json.loads(request.get_data().decode())))) 
