from . import entity

def add_order(order):
    order.save()
    return order