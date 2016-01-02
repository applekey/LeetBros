
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,run,static_file

@route('/')
def hello_world():
    return static_file('start.html', root='static/html')

@route('/shtml/<filename>')
def server_static(filename):
    return static_file(filename, root='static/html')

@route('/template/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/startbootstrap-sb-admin-2-gh-pages/')

application = default_app()

run(host='localhost', port=8000)
