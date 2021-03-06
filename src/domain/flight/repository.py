from . import entity
from mongoengine.queryset.visitor import Q
from datetime import datetime, timedelta

def get_all_flights():
    return entity.Flight.objects()

def get_flight(route, departure_time):
    return entity.Flight.objects(Q(route=route) & Q(departure_time=departure_time)).first()

def get_flight_with_route(route):
    return entity.Flight.objects(route=route)

def get_flight_with_number_of_seats(route, departure_date, number_of_seats):
    target_date = datetime.strptime(departure_date, "%Y-%m-%d")
    return entity.Flight.objects(Q(route=route) 
        & Q(departure_time__gte=target_date)
        & Q(departure_time__lte=target_date + timedelta(hours=23, minutes=59, seconds=59))
        & Q(max_capacity__gte=number_of_seats)).order_by('price')

def add_flight(flight):
    flight.save()
    return flight

def delete_flight(flight):
    flight.delete()
    return

def update_flight(flight, update_flight):
    for key, value in update_flight.items():
        if value is not None:
            flight[key] = value
    flight.save()
    return flight

def get_flight_by_public_id(public_id):
    return entity.Flight.objects(public_id=public_id).get_or_404()

def get_flight_with_number_of_seats_and_public_id(public_id, number_of_seats):
    return entity.Flight.objects(Q(public_id=public_id) 
        & Q(max_capacity__gte=number_of_seats)).get_or_404()