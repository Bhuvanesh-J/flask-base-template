from flask import Blueprint, request

from authentication.views import signup_views, login_views, logout_views
from student.models import Student

authentication = Blueprint('authentication-api', __name__, url_prefix='/api/v1/authentication/')



@authentication.route('signup', methods=['POST'])
def signup_controller():
    s = Student()

    return signup_views(request)


@authentication.route('login', methods=['POST'])
def login_controller():
    return login_views(request)


@authentication.route('logout', methods=['POST'])
def logout_controller():
    return logout_views(request)
