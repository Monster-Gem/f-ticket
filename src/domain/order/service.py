from . import repository
from werkzeug.exceptions import Conflict, NotFound
from .order_status import OrderStatus

def make_reservation(customer, order):
    order.customer = customer
    order.status = OrderStatus.RESERVED
    return repository.add_order(order)