from flask import Blueprint

main = Blueprint('main', __name__, template_folder='main')

from app.main import views, forms
