from domain.flight import entity
from flask_mongoengine import BaseQuerySet
from domain.route.service import get_route
from domain.route.dtos import json_from_route
from domain.airport.service import get_airport
from decimal import Decimal

def args_to_price(args):
    return args.get('price', None)

def args_to_max_capacity(args):
    return args.get('max_capacity', None)

def args_to_route(args):
    route_origin_name = args.get("route", {"origin": None}).get('origin')
    route_destination_name = args.get("route", {"destination": None}).get('destination')
    return None if route_origin_name or route_destination_name is None else get_route(route_origin_name, route_destination_name)

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