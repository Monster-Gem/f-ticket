from domain.route import entity
from flask_mongoengine import BaseQuerySet
from domain.airport.service import get_airport
from domain.airport.dtos import json_from_airport, json_from_airports

def args_to_origin(args):
    origin_name = args.get('origin', None)
    return None if origin_name is None else get_airport(origin_name)

def args_to_destination(args):
    destination_name = args.get('destination', None)
    return None if destination_name is None else get_airport(destination_name)

def json_to_update_route(route_json):
    origin_name = route_json.get('origin', {'name': None}).get('name')
    destination_name = route_json.get('destination', {'name': None}).get('name')
    return {
        'origin': get_airport(origin_name) if origin_name else None,
        'destination': get_airport(destination_name) if destination_name else None
    }

def json_from_route(route):
    return {
        "origin": json_from_airport(route.origin), 
        "destination": json_from_airport(route.destination)
    }

def json_from_routes(routes):
    return {'routes': list(map(json_from_route, routes))} if isinstance(routes, BaseQuerySet) else json_from_route(routes)

def json_from_destination(route):
    return json_from_airports(route.destination)

def json_from_destinations(routes):
    return {'destinations': list(map(json_from_destination, routes))} if isinstance(routes, BaseQuerySet) else json_from_destination(routes)

def route_from_json(route_json):
    return entity.Route(
        origin=get_airport(route_json.get('origin', None).get('name', None)),
        destination=get_airport(route_json.get('destination', None).get('name', None)))