from flask import Blueprint
from flask_login import login_required
from app.models import Pet

pet_routes = Blueprint(('pets', __name__))

# 