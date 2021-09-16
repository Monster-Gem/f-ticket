from domain.maintenance.repository import database

class User(database.Document):
    email = database.StringField(required=True, max_length=320, unique=True)
    password = database.StringField(required=True, max_length=128)
    token = database.StringField()
    token_create = database.DateTimeField()