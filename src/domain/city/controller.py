from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import admin_required
import json

city = Blueprint('city', __name__, url_prefix='/cities')

@city.route('', methods = ['POST'])
@admin_required
def add_city(authenticated_user):
    return dtos.json_from_city(service.add_city(dtos.city_from_json(request.get_json())))

@city.route('', methods = ['GET'])
@admin_required
def get_cities(authenticated_user):
    return dtos.json_from_cities(service.get_cities(dtos.args_to_name(request.args)))

@city.route('', methods = ['DELETE'])
@admin_required
def delete_city(authenticated_user):
    service.delete_city(dtos.args_to_name(request.args))
    return {}

@city.route('', methods = ['PATCH'])
@admin_required
def update_city(authenticated_user):
    return dtos.json_from_cities(service.update_city(dtos.args_to_name(request.args), dtos.json_to_update_city(json.loads(request.get_data().decode())))) 
