from domain.city import entity
from flask_mongoengine import BaseQuerySet

def args_to_name(args):
    return args.get('name', None)

def json_to_update_city(city_json):
    return { 'name': city_json.get('name', None)}

def json_from_city(city):
    return {"name": city.name}

def json_from_cities(cities):
    return {"cities": list(map(json_from_city, cities))} if isinstance(cities, BaseQuerySet) else json_from_city(cities)

def city_from_json(city_json):
    return entity.City(name=city_json.get('name'))