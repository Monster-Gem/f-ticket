from flask import Flask
from domain.maintenance.controller import maintenance

app = Flask(__name__)
app.register_blueprint(maintenance)

if __name__ == '__main__':
    app.run(debug=True)