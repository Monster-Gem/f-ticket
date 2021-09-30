from . import entity
from mongoengine.queryset.visitor import Q

def add_ticket(ticket):
    ticket.save()
    return ticket

def get_all_tickets_from_order(order):
    return entity.Ticket.objects(order=order)

def delete_all_tickets_with_order(order):
    entity.Ticket.objects(order=order).delete()
    return