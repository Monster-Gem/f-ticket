from . import repository
from werkzeug.exceptions import Conflict, NotFound
from .order_status import OrderStatus
from domain.flight.service import increase_max_capacity, decrease_max_capacity

def make_reservation(customer, order):
    order.customer = customer
    order.status = OrderStatus.RESERVED
    decrease_max_capacity(order.flight, order.number_of_seats)
    return repository.add_order(order)

def confirm_reservation(customer, public_id):
    order = get_order(customer, public_id)
    order.status = OrderStatus.FINISHED
    return repository.add_order(order)

def get_orders(customer, order_id=None):
    if customer and order_id:
        return get_order(customer, order_id)
    else:
        return repository.get_all_orders_from_user(customer)

def get_order(customer, public_id):
    return repository.get_order_with_user_and_public_id(customer, public_id)

def delete_order(customer, public_id):
    order = get_order(customer, public_id)
    flight = order.flight
    number_of_seats = order.number_of_seats
    repository.delete_order(order)
    increase_max_capacity(flight, number_of_seats)
    return