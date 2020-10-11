from flask import Blueprint

error = Blueprint('error', __name__, template_folder='error')

from app.error import views
