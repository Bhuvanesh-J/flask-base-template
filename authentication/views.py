import traceback

from sqlalchemy.orm import load_only
from werkzeug.security import generate_password_hash, check_password_hash

from authentication.froms import SignupValidation, LoginValidation
from common.responses import response
from common.views import commit_object_to_db
from student.models import Student


def signup_views(request):
    try:
        payload = request.get_json()

        try:
            schema = SignupValidation()
            schema.load(payload)
        except Exception as e:
            return response('create', 'failed', e.messages, "Mandatory keys are missing!!")

        if bool(Student.query.filter_by(email=payload['email']).first()):
            return response('create', 'failed', {}, "Email id already exists!!")
        save_to_student(payload)

        return response('create', 'success', {})
    except Exception as e:
        return response('create', 'failed', {}, str(e))


def login_views(request):
    try:
        payload = request.get_json()

        try:
            form_obj = LoginValidation()
            form_obj.load(payload)
        except Exception as e:
            return response('create', 'failed', e.messages, "Mandatory keys are missing!!")
        # data = Student.query.filter_by(email=payload['email']).all()[0]
        fields = ['_id', 'email', 'hashed_password']
        data = Student.query.filter_by(email=payload['email']).options(load_only(*fields)).all()[0]
        if not data:
            return response('retrieve', 'failed', {}, 'Email id does not exists')
        if not check_password_hash(pwhash=data.hashed_password, password=payload['password']):
            return response('retrieve', 'unauthorized', {}, 'Invalid Password')
        result = {}
        obj = Student()
        result['access_token'] = (obj.generate_access_token(data))
        result['refresh_token'] = (obj.generate_refresh_token(data))

        return response('retrieve', 'success', {"data":result})
    except Exception as e:
        print(traceback.format_exc())
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
        student_obj.hashed_password = password
    if 'gender' in payload and payload['gender']:
        student_obj.gender = payload['gender']
    if 'dob' in payload and payload['dob']:
        student_obj.dob = payload['dob']
    return commit_object_to_db(student_obj)
