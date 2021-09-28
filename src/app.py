from settings import DATABASE_NAME, DATABASE_HOST, DATABASE_PORT, SECRET_KEY
from flask import Flask
from domain.maintenance.controller import maintenance
from domain.maintenance.repository import database
from domain.auth.controller import auth
from domain.city.controller import city
from domain.airport.controller import airport
from domain.user.controller import user

app = Flask(__name__)

app.register_blueprint(maintenance)
app.register_blueprint(user)
app.register_blueprint(auth)
app.register_blueprint(city)
app.register_blueprint(airport)

app.config['MONGODB_SETTINGS'] = {
    'db':DATABASE_NAME,
    'host':DATABASE_HOST,
    'port':DATABASE_PORT
}

app.config['SECRET_KEY'] = SECRET_KEY

database.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)