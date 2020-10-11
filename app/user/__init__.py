from flask import Blueprint

user = Blueprint('user', __name__, template_folder='user')

from app.user import views, forms
