from domain.maintenance.repository import database
import uuid

class City(database.Document):
    public_id = database.StringField(max_length=50, unique = True, default=str(uuid.uuid4()))
    name = database.StringField(required=True, max_length=58, unique=True)