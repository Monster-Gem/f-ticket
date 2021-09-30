from domain.user.entity import User
from domain.flight.entity import Flight
from domain.maintenance.repository import database
from .order_status import OrderStatus
import uuid

def _bigger_than_zero(value):
    if value <= 0:
        raise database.ValidationError('value cannot be zero')

class Order(database.Document):
    public_id = database.StringField(max_length=50, unique = True, default=lambda: str(uuid.uuid4()))
    status = database.EnumField(OrderStatus, default=OrderStatus.RESERVED)
    flight = database.ReferenceField(Flight)
    customer = database.ReferenceField(User, unique_with='flight')
    number_of_seats = database.IntField(default=1, validation=_bigger_than_zero)