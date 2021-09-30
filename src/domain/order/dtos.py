from flask_mongoengine import BaseQuerySet
from werkzeug.security import generate_password_hash
from domain.order import entity
from domain.flight.service import get_flight_with_number_of_seats_and_public_id
from werkzeug.exceptions import BadRequest
from domain.user.dtos import json_from_user

def reservation_from_json(reservation_json):
    number_of_seats = reservation_json.get('number_of_seats')
    flight_id = reservation_json.get('flight_id')
    if not (number_of_seats and flight_id):
        raise BadRequest('Missing number of seats and/or flight id')
    else: 
        return entity.Order(
            number_of_seats=number_of_seats,
            flight=get_flight_with_number_of_seats_and_public_id(flight_id, number_of_seats))

def json_from_orders(orders):
    return {'orders': list(map(json_from_order, orders))} if isinstance(orders, BaseQuerySet) else json_from_order(orders)


def json_from_order(order):
    return {
        "order_id": order.public_id,
        "status": str(order.status.value),
        "customer": json_from_user(order.customer),
        "number_of_seats": order.number_of_seats
    }

def args_to_public_id(args):
    return args.get('order_id', None)