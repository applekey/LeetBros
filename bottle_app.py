
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app,run,app
## custom imports
from routes import *

from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'cookie',
    'session.data_dir': './session/',
    'session.validate_key' : 'validateplz',
    'session.encrypt_key' : 'encryptplz',
    'session.auto': True
}

application = SessionMiddleware(default_app(), session_opts)

if __name__ == "__main__":
	run(app=application, reloader=True,debug=True, host='localhost', port=8080)
