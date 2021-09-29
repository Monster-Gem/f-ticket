from . import entity
from mongoengine.queryset.visitor import Q

def get_all_flights():
    return entity.Flight.objects()

def get_flight(route, departure_time):
    return entity.Flight.objects(Q(route__origin=route.origin) & Q(route__destination=route.destination) & Q(departure_time=departure_time)).first()

def add_flight(flight):
    flight.save()
    return flight

def delete_flight(flight):
    flight.delete()
    return

def update_flight(flight, update_flight):
    for key, value in update_flight.items():
        if value:
            flight[key] = value
    flight.save()
    return flight