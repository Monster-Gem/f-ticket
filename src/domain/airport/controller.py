 
from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import admin_required, user_required
import json

airport = Blueprint('airport', __name__, url_prefix='/airports')

@airport.route('', methods = ['POST'])
@admin_required
def add_airport(authenticated_user):
    return dtos.json_from_airport(service.add_airport(dtos.airport_from_json(request.get_json())))

@airport.route('', methods = ['GET'])
@user_required
def get_airports(authenticated_user):
    return dtos.json_from_airports(service.get_airports(dtos.args_to_name(request.args)))

@airport.route('', methods = ['DELETE'])
@admin_required
def delete_airport(authenticated_user):
    service.delete_airport(dtos.args_to_name(request.args))
    return {}

@airport.route('', methods = ['PATCH'])
@admin_required
def update_airport(authenticated_user):
    return dtos.json_from_airports(service.update_airport(dtos.args_to_name(request.args), dtos.json_to_update_airport(json.loads(request.get_data().decode())))) 
