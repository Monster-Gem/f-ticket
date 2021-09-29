from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_flights(route=None, departure_time=None):
    return get_flight(route, departure_time) if route is not None and departure_time is not None else repository.get_all_flights()

def get_flight(route, departure_time):
    flight = repository.get_flight(route, departure_time)
    if not flight:
        raise NotFound('Flight does not exists.')
    else:
        return flight

def add_flight(flight):
    try:
        get_flight(flight.route, flight.departure_time)
        raise Conflict('Flight already exists.')
    except NotFound:
        return repository.add_flight(flight)

def delete_flight(route, departure_time):
    repository.delete_flight(get_flight(route, departure_time))
    return

def update_flight(route, departure_time, update_flight):
    return repository.update_flight(get_flight(route, departure_time), update_flight)