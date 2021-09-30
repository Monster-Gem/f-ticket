from . import entity

def add_ticket(ticket):
    ticket.save()
    return ticket

def get_all_tickets_from_user(user):
    return entity.Ticket.objects(order__customer=user)

def delete_all_tickets_with_order(order):
    entity.Ticket.objects(order=order).delete()
    return

def get_ticket_with_user_and_public_id(user, public_id):
    return entity.Ticket.objects(public_id=public_id, order__customer=user).get_or_404()