from . import repository
from . import entity

def create_tickets(order, number_of_tickets):
    tickets = []
    while number_of_tickets > 0:
        tickets.append(repository.add_ticket(entity.Ticket(order=order)))
        number_of_tickets -= 1
    return tickets

def delete_tickets(order):
    repository.delete_all_tickets_with_order(order)
    return

def get_tickets_from_order(order):
    return repository.get_all_tickets_from_order(order)
