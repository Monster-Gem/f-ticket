from domain.maintenance.repository import database
from .user_roles import UserRoles
import uuid

class User(database.Document):
    public_id = database.StringField(max_length=50, unique = True, default=lambda: str(uuid.uuid4()))
    email = database.StringField(required=True, max_length=320, unique=True)
    password = database.StringField(required=True, max_length=128)
    role = database.EnumField(UserRoles, default=UserRoles.USER)
    last_valid_token = database.StringField()
