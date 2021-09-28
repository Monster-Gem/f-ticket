from . import repository
from werkzeug.exceptions import Conflict, NotFound

def get_routes(origin=None, destination=None):
    if origin and destination:
        return get_route(origin, destination)
    elif origin is not None and destination is None:
        return repository.get_route_with_origin(origin)
    elif destination is not None and origin is None:
        return repository.get_route_with_destination(destination)
    else:
        return repository.get_all_routes()

def get_route(origin, destination):
    route = repository.get_route(origin, destination)
    if not route:
        raise NotFound('Route does not exists.')
    else:
        return route

def add_route(route):
    try:
        get_route(route.origin, route.destination)
        raise Conflict('Route already exists.')
    except NotFound:
        return repository.add_route(route)

def delete_route(origin, destination):
    repository.delete_route(get_route(origin, destination))
    return

def update_route(origin, destination, update_route):
    return repository.update_route(get_route(origin, destination), update_route)