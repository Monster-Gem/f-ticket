from domain.maintenance.repository import database
import uuid
from domain.city.entity import City

class Airport(database.Document):
    name = database.StringField(required=True, max_length=58, unique=True)
    city = database.ReferenceField(City)