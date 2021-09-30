from flask import Blueprint, request
from . import dtos, service
from domain.auth.decorators import user_required
import json

ticket = Blueprint('ticket', __name__, url_prefix='/tickets')

@ticket.route('', methods = ['GET'])
@user_required
def get_tickets(authenticated_user):
    return dtos.json_from_tickets(
        service.get_tickets(
            authenticated_user,
            dtos.args_to_public_id(request.args)))