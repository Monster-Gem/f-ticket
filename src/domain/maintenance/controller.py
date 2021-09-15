from domain import maintenance


from flask import Blueprint

maintenance = Blueprint('maintenance', __name__, url_prefix='/maintenance')

@maintenance.route('/health-check')
def health_check():
    return "Pass"