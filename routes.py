from bottle import route,static_file
import sys,os
attachmentDirectory = os.path.join(os.getcwd(),'attachments')
sys.path.append(attachmentDirectory)
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
    if function == 'addTenant':
        return 'tenantAdded'
