from settings import DATABASE_NAME, DATABASE_HOST, DATABASE_PORT
from flask import Flask
from domain.maintenance.controller import maintenance
from domain.maintenance.repository import database
from domain.user.controller import user

app = Flask(__name__)

app.register_blueprint(maintenance)
app.register_blueprint(user)

app.config['MONGODB_SETTINGS'] = {
    'db':DATABASE_NAME,
    'host':DATABASE_HOST,
    'port':DATABASE_PORT
}

database.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)