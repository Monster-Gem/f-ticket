from . import entity

def get_all_airports():
    return entity.Airport.objects()

def get_airport(name):
    return entity.Airport.objects(name=name).first()

def get_airport_by_public_id(public_id):
    return entity.Airport.objects(public_id=public_id).get_or_404()

def add_airport(airport):
    airport.save()
    return airport

def delete_airport(airport):
    airport.delete()
    return

def update_airport(airport, update_airport):
    for key, value in update_airport.items():
        if value:
            airport[key] = value
    airport.save()
    return airport