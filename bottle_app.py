
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route,run,static_file
## custom imports
import sys
sys.path.append("attachments/")
from emailAdapter import *

@route('/')
def hello_world():
    return static_file('start.html', root='static/html')

@route('/shtml/<filename>')
def server_static(filename):
    return static_file(filename, root='static/html')

@route('/js/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/js/')

@route('/template/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/startbootstrap-sb-admin-2-gh-pages/')

@route('/functions/<function>')
def server_static(function):
    if function == 'attachments':
        emailad = emailAdapter('applekeyhousing@gmail.com','vancouver!@#')
        emailad.connect()
        attachments = emailad.listAttachments()
        emailad.disconnect()
        return attachments

application = default_app()

run(reloader=True,debug=True, host='localhost', port=8001)
