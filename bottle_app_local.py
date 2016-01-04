
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app,run
## custom imports
from routes import *

application = default_app()

run(reloader=True,debug=True, host='localhost', port=8080)
