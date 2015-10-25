
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,run,static_file

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

application = default_app()

#run(host='localhost', port=8080)
