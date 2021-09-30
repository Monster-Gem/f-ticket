from domain.maintenance.repository import database
import uuid

class City(database.Document):
    name = database.StringField(required=True, max_length=58, unique=True)