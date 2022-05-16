from werkzeug.security import generate_password_hash, check_password_hash

from common.responses import response


def signup_views(request):
    try:
        generate_password_hash(password="dhwd")
        return response('create', 'success', {})
    except Exception as e:
        return response('create', 'success', {}, str(e))


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
