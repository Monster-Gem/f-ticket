from domain.airport import entity
from flask_mongoengine import BaseQuerySet
from domain.city.service import get_city
from domain.city.dtos import json_from_city

def args_to_name(args):
    return args.get('name', None)

def json_to_update_airport(airport_json):
    city_name = airport_json.get('city', {'name': None}).get('name')
    return {
        'name': airport_json.get('name', None),
        'city': get_city(city_name) if city_name else None
    }

def json_from_airport(airport):
    return {'name': airport.name, "city": json_from_city(airport.city)}

def json_from_airports(airports):
    return {'airports': list(map(json_from_airport, airports))} if isinstance(airports, BaseQuerySet) else json_from_airport(airports)

def airport_from_json(airport_json):
    return entity.Airport(
        name=airport_json.get('name'), 
        city=get_city(airport_json.get('city', None).get('name', None)))