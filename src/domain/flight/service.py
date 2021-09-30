from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_flights(route=None, departure_date=None, number_of_seats=None):
    if route and departure_date and number_of_seats:
        return repository.get_flight_with_number_of_seats(route, departure_date, number_of_seats)
    elif route and departure_date and not number_of_seats:
        return get_flight(route, departure_date)
    elif not route and departure_date and not number_of_seats:
        return repository.get_flight_with_departure_date(departure_date)
    elif route and not departure_date and not number_of_seats:
        return repository.get_flight_with_route(route)
    else:
        return repository.get_all_flights()

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