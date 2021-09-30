from . import entity

def add_order(order):
    order.save()
    return order

def get_all_orders_from_user(user):
    return entity.Order.objects(customer=user)

def get_order_with_user_and_public_id(user, public_id):
    return entity.Order.objects(public_id=public_id, customer=user).get_or_404()

def delete_order(order):
    order.delete()
    return