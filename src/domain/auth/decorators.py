from settings import SECRET_KEY
from flask import request
from domain.user.service import get_user_by_public_id
from domain.user.user_roles import UserRoles
from werkzeug.exceptions import Unauthorized
from jwt import decode
from functools import wraps

def user_required(function):
    @wraps(function)
    def verify_user(*args, **kwargs):
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].replace('Bearer ', '')
        else:
            raise Unauthorized('Token is missing')
        try:
            data = decode(token, SECRET_KEY)
            authenticated_user = get_user_by_public_id(data['public_id'])
            if authenticated_user.last_valid_token != token:
                raise Unauthorized()
        except:
            raise Unauthorized('Token is invalid')
        return function(authenticated_user, *args, **kwargs)
    return verify_user

def admin_required(function):
    @wraps(function)
    @user_required
    def verify_admin(authenticated_user, *args, **kwargs):
        if not authenticated_user:
            raise Unauthorized('User is missing')
        if authenticated_user.role != UserRoles.ADMIN:
            raise Unauthorized('User is not an Admin')
        return function(authenticated_user, *args, **kwargs)
    return verify_admin