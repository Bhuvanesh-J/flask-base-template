from flask import session
from werkzeug.security import generate_password_hash, check_password_hash

from common.responses import response
from common.views import commit_object_to_db
from student.models import Student


def signup_views(request):
    try:
        payload = request.get_json()
        if 'email' in payload and payload['email']:
            try:
                session.query(Student).get(email=payload['email'])
            except Exception as e:
                print(e)
                return response('create', 'failed', {}, "Email already exists")
        save_to_student(payload)

        return response('create', 'success', {})
    except Exception as e:
        return response('create', 'failed', {}, str(e))


def login_views(request):
    try:
        if not check_password_hash(pwhash="fbhefbhef", password="fbrbfb"):
            return response('retrieve', 'unauthorized', {}, 'Invalid Password')

        return response('retrieve', 'success', {})
    except Exception as e:
        return response('retrieve', 'failed', {}, str(e))


def logout_views(request):
    try:
        return response('create', 'success', {}, "Logout Successful")
    except Exception as e:
        return response('create', 'failed', {}, str(e))


def save_to_student(payload):
    student_obj = Student()
    if 'first_name' in payload and payload['first_name']:
        student_obj.first_name = payload['first_name']
    if 'last_name' in payload and payload['last_name']:
        student_obj.last_name = payload['last_name']
    if 'email' in payload and payload['email']:
        student_obj.email = payload['email']
    if 'password' in payload and payload['password']:
        password = generate_password_hash(password=payload['password'])
        student_obj.hashed_password = password[0:18]
    if 'gender' in payload and payload['gender']:
        student_obj.gender = payload['gender']
    if 'dob' in payload and payload['dob']:
        student_obj.dob = payload['dob']
    student_obj.deleted_at = payload['dob']

    return commit_object_to_db(student_obj)
