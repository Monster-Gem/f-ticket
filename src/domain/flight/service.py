from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_flights(route=None, departure_date=None, number_of_seats=None):
    if route and departure_date and number_of_seats:
        return repository.get_flight_with_number_of_seats(route, departure_date, number_of_seats)
    elif route and departure_date:
        return repository.get_flight_with_number_of_seats(route, departure_date, 0)
    elif route:
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

def get_flight_by_public_id(public_id):
    return repository.get_flight_by_public_id(public_id)

def get_flight_with_number_of_seats_and_public_id(public_id, number_of_seats):
    return repository.get_flight_with_number_of_seats_and_public_id(public_id, number_of_seats)

def increase_max_capacity(flight, delta):
    return repository.update_flight(flight, {'max_capacity': flight.max_capacity + delta})

def decrease_max_capacity(flight, delta):
    new_capacity = flight.max_capacity - delta
    if new_capacity < 0:
        raise Conflict('Max capacity reached')
    return repository.update_flight(flight, {'max_capacity': new_capacity})