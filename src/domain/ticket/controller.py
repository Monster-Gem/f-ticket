from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import user_required
import json

ticket = Blueprint('ticket', __name__, url_prefix='/tickets')

@ticket.route('', methods = ['GET'])
@user_required
def get_tickets(authenticated_user):
    return dtos.json_from_tickets(
            service.get_tickets_from_order(
            dtos.args_to_order(authenticated_user, request.args)))