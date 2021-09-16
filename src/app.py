from settings import DATABASE_NAME, DATABASE_HOST, DATABASE_PORT
from flask import Flask
from domain.maintenance.controller import maintenance
from domain.maintenance.repository import database

app = Flask(__name__)

app.register_blueprint(maintenance)

app.config['MONGODB_SETTINGS'] = {
    'db':DATABASE_NAME,
    'host':DATABASE_HOST,
    'port':DATABASE_PORT
}

database.init_app()

if __name__ == '__main__':
    app.run(debug=True)