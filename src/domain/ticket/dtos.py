from flask_mongoengine import BaseQuerySet

def args_to_public_id(args):
    return args.get('ticket_id', None)

def json_from_tickets(tickets):
    return {'tickets': list(map(json_from_ticket, tickets))} if isinstance(tickets, BaseQuerySet) else json_from_ticket(tickets)

def json_from_ticket(ticket):
    return {
        "ticket_id": ticket.public_id
    }
