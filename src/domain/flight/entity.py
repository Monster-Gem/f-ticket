from domain.maintenance.repository import database
import uuid

class Flight(database.Document):
    public_id = database.StringField(max_length=50, unique = True, default=str(uuid.uuid4()))
    price = database.DecimalField(required=True, decimal_places=2)
    max_capacity = database.IntField(required=True)
    # route = database.IntField(required=True)
    departure_time = database.DateTimeField(required=True)