from flask import request

from common.responses import response


def middleware(app):
    @app.before_request
    def process_request():
        try:
            # request.endpoint,request.url,request.path
            api = ((request.path).split('?')[0]).split('/')
            if api[-1] in ['signup']:
                pass
            else:
                return response('create', 'unauthorized', {})
        except Exception as e:
            print(e)
            return response('create', 'unauthorized', {}, str(e))


def validate_auth_token(token):
    try:
        return 1
    except Exception as e:
        return -1
