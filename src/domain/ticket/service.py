from . import repository
from . import entity

def create_tickets(order, number_of_tickets):
    tickets = []
    while number_of_tickets > 0:
        tickets.append(repository.add_ticket(entity.Ticket(order=order)))
        number_of_tickets -= 1
    return tickets

def delete_tickets(order):
    repository.delete_tickets_with_order(order)
    return

def get_tickets(customer, ticket_id=None):
    if customer and ticket_id:
        return get_ticket(customer, ticket_id)
    else:
        return repository.get_all_tickets_from_user(customer)

def get_ticket(customer, public_id):
    return repository.get_ticket_with_user_and_public_id(customer, public_id)
