from flask_mongoengine import BaseQuerySet
from werkzeug.security import generate_password_hash
from domain.order import entity
from werkzeug.exceptions import BadRequest

def reservation_from_json(reservation_json):
    number_of_seats = reservation_json.get('number_of_seats')
    if not number_of_seats:
        raise BadRequest('Missing number of seats')
    else: 
        return entity.Order(number_of_seats=number_of_seats)

def json_from_order(order):
    return {
        "public_id": order.public_id,
        "status": order.status,
        "customer": order.customer.email,
        "number_of_seats": order.number_of_seats
    }