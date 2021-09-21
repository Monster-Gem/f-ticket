from . import entity

def get_all_users():
    return entity.User.objects()

def get_user(email):
    return entity.User.objects(email=email).first()

def get_user_by_public_id(public_id):
    return entity.User.objects(public_id=public_id).get_or_404()

def add_user(user):
    user.save()
    return user

def delete_user(user):
    user.delete()
    return

def update_user(user, update_user):
    for key, value in update_user.items():
        if value:
            user[key] = value
    user.save()
    return user