from . import entity
from mongoengine.queryset.visitor import Q

def get_all_routes():
    return entity.Route.objects()

def get_route_with_origin(origin):
    return entity.Route.objects(origin=origin).first()

def get_route_with_destination(destination):
    return entity.Route.objects(destination=destination).first()

def get_route(origin, destination):
    return entity.Route.objects(Q(origin=origin) & Q(destination=destination)).first()

def add_route(route):
    route.save()
    return route

def delete_route(route):
    route.delete()
    return

def update_route(route, update_route):
    for key, value in update_route.items():
        if value:
            route[key] = value
    route.save()
    return route