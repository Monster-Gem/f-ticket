from flask_mongoengine import BaseQuerySet
from domain.order.service import get_order

def args_to_order(authenticated_user, args):
    return get_order(authenticated_user, args.get('order_id', None))

def json_from_tickets(tickets):
    return {'tickets': list(map(json_from_ticket, tickets))} if isinstance(tickets, BaseQuerySet) else json_from_ticket(tickets)

def json_from_ticket(ticket):
    return {
        "ticket_id": ticket.public_id
    }
