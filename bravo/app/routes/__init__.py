from flask import Blueprint

routes_bp = Blueprint('routes', __name__)

from . import index, login
