from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import user_required
import json

order = Blueprint('order', __name__, url_prefix='/orders')

@user.route('/reservation', methods = ['POST'])
@user_required
def make_reservation(authenticated_user):
    return dtos.json_from_order(service.make_reservation(authenticated_user, dtos.reservation_from_json(request.get_json())))