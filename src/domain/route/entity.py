from domain.maintenance.repository import database
import uuid
from domain.airport.entity import Airport

class Route(database.Document):
    origin = database.ReferenceField(Airport)
    destination = database.ReferenceField(Airport, unique_with='origin')