from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import user_required
import json

order = Blueprint('order', __name__, url_prefix='/orders')

@order.route('/reservation', methods = ['POST'])
@user_required
def make_reservation(authenticated_user):
    return dtos.json_from_order(service.make_reservation(authenticated_user, dtos.reservation_from_json(request.get_json())))

@order.route('/confirmation', methods = ['POST'])
@user_required
def confirm_reservation(authenticated_user):
    return dtos.json_from_order(
        service.confirm_reservation(
            authenticated_user,
            dtos.args_to_public_id(request.args)))

@order.route('', methods = ['GET'])
@user_required
def get_orders(authenticated_user):
    return dtos.json_from_orders(
        service.get_orders(
            authenticated_user,
            dtos.args_to_public_id(request.args)))

@order.route('', methods = ['DELETE'])
@user_required
def delete_order(authenticated_user):
    service.delete_order(
        authenticated_user,
        dtos.args_to_public_id(request.args))
    return {}