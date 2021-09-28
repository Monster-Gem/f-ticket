from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_cities(name=None):
    return get_city(name) if name is not None else repository.get_all_cities()

def get_city(name):
    city = repository.get_city(name)
    if not city:
        raise NotFound('City does not exists.')
    else:
        return city

def add_city(city):
    try:
        get_city(city.name)
        raise Conflict('City already exists.')
    except NotFound:
        return repository.add_city(city)

def delete_city(name):
    repository.delete_city(get_city(name))
    return

def update_city(name, update_city):
    return repository.update_city(get_city(name), update_city)