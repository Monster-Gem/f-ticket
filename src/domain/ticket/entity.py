from domain.order.entity import Order
from domain.maintenance.repository import database
import uuid

class Ticket(database.Document):
    public_id = database.StringField(max_length=50, unique = True, default=lambda: str(uuid.uuid4()))
    order = database.ReferenceField(Order)