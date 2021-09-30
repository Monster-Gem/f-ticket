from enum import unique
from domain.maintenance.repository import database
import uuid
from domain.route.entity import Route

class Flight(database.Document):
    price = database.DecimalField(required=True, decimal_places=2)
    max_capacity = database.IntField(required=True)
    route = database.ReferenceField(Route)
    departure_time = database.DateTimeField(required=True, unique_with='route')