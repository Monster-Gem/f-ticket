from . import entity

def get_all_cities():
    return entity.City.objects()

def get_city(name):
    return entity.City.objects(name=name).first()

def get_city_by_public_id(public_id):
    return entity.City.objects(public_id=public_id).get_or_404()

def add_city(city):
    city.save()
    return city

def delete_city(city):
    city.delete()
    return

def update_city(city, update_city):
    for key, value in update_city.items():
        if value:
            city[key] = value
    city.save()
    return city