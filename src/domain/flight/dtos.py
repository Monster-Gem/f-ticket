from domain.flight import entity
from flask_mongoengine import BaseQuerySet
from domain.route.service import get_routes
from domain.route.dtos import json_from_route
from domain.airport.service import get_airport
from decimal import Decimal

def args_to_price(args):
    return args.get('price', None)

def args_to_max_capacity(args):
    return args.get('max_capacity', None)

def args_to_route(args):
    origin_name = args.get("origin", None)
    destination_name = args.get("destination", None)
    origin = get_airport(origin_name) if origin_name else None
    destination = get_airport(destination_name) if destination_name else None
    return get_routes(origin, destination) if origin or destination else None

def args_to_departure_time(args):
    return args.get('departure_time', None)

# Fazer o update

def json_from_flight(flight):
    return {
        'price': str(flight.price),
        'max_capacity': flight.max_capacity,
        "route": json_from_route(flight.route), 
        'departure_time': flight.departure_time
    }

def json_from_flights(flights):
    return {'flights': list(map(json_from_flight, flights))} if isinstance(flights, BaseQuerySet) else json_from_flight(flights)

def flight_from_json(flight_json):
    route_json = flight_json.get('route', None)
    return entity.Flight(
        price=flight_json.get('price'), 
        max_capacity=flight_json.get('max_capacity'), 
        route=get_route(
            get_airport(route_json.get('origin', {"name": None}).get('name')),
            get_airport(route_json.get('destination', {"name": None}).get('name'))),
        departure_time=flight_json.get('departure_time'))

def json_to_update_flight(flight_json):
    route = flight_json.get('route', {'origin': {'name': None}, 'destination': {'name': None}})
    origin_name = route.get('origin').get('name')
    destination_name = route.get('destination').get('name')
    return {
        'price': flight_json.get('price', None),
        'max_capacity': flight_json.get('max_capacity', None),
        'departure_time': flight_json.get('departure_time', None),
        'route': get_route(origin_name, destination_name) if origin_name and destination_name else None,
    }