from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import admin_required, user_required
import json

flight = Blueprint('flight', __name__, url_prefix='/flights')

@flight.route('', methods = ['POST'])
@admin_required
def add_flight(authenticated_user):
    return dtos.json_from_flight(
        service.add_flight(
            dtos.flight_from_json(request.get_json())))

@flight.route('', methods = ['GET'])
@user_required
def get_flights(authenticated_user):
    return dtos.json_from_flights(
        service.get_flights(
            dtos.args_to_route(request.args), 
            dtos.args_to_departure_date(request.args),
            dtos.args_to_max_capacity(request.args)))

@flight.route('', methods = ['DELETE'])
@admin_required
def delete_flight(authenticated_user):
    service.delete_flight(
        dtos.args_to_route(request.args), 
        dtos.args_to_departure_time(request.args))
    return {}
    
@flight.route('', methods = ['PATCH'])
@admin_required
def update_flight(authenticated_user):
    return dtos.json_from_flights(
        service.update_flight(
            dtos.args_to_route(request.args), 
            dtos.args_to_departure_time(request.args),
            dtos.json_to_update_flight(json.loads(request.get_data().decode()))))
