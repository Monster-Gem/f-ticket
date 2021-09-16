from . import entity

def get_all_users():
    return entity.User.objects()

def get_user(email):
    return entity.User.objects(email=email).get_or_404()

def add_user(user):
    user.save()
    return user

def delete_user(user):
    user.delete()
    return

def update_user(user):
    user.update()
    return user