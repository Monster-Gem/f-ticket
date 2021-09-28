from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_airports(name=None):
    return get_airport(name) if name is not None else repository.get_all_airports()

def get_airport_by_public_id(public_id):
    return repository.get_airport_by_public_id(public_id)

def get_airport(name):
    airport = repository.get_airport(name)
    if not airport:
        raise NotFound('Airport does not exists.')
    else:
        return airport

def add_airport(airport):
    try:
        get_airport(airport.name)
        raise Conflict('Airport already exists.')
    except NotFound:
        return repository.add_airport(airport)

def delete_airport(name):
    repository.delete_airport(get_airport(name))
    return

def update_airport(name, update_airport):
    return repository.update_airport(get_airport(name), update_airport)