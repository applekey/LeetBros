from bottle import route,static_file,post,request
import sys,os
attachmentDirectory = os.path.join(os.getcwd(),'attachments')
dbDirectory = os.path.join(os.getcwd(),'db')
sys.path.append(attachmentDirectory)
sys.path.append(dbDirectory)
from emailAdapter import *
from peopleAdapter import *
from peopleContainer import *

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

@route('/addTenant', method='POST')
def do_login():
    print 'hererererre'
    tenantName = request.forms.get('tenantName')
    tenantEmail = request.forms.get('tenantEmail')
    #create container for db entry
    container = peopleContainer((tenantName)
                                ,(tenantEmail))
    print tenantName + tenantEmail

    ##fixifixifix mofomomomomfoo
    username = 'applekey'
    password = 'vancouver!@#'
    host = "applekey.mysql.pythonanywhere-services.com"
    database = 'applekey$housing'

    pplAdapter =peopleAdapter(username,password,host,database)
    pplAdapter.connect()
    pplAdapter.createClient(container)
    pplAdapter.disconnect()
    print 'done'


@route('/functions/<function>')
def server_static(function):
    pass
    # if function == 'attachments':
    #     emailad = emailAdapter('applekeyhousing@gmail.com','vancouver!@#')
    #     emailad.connect()
    #     attachments = emailad.listAttachments()
    #     emailad.disconnect()
    #     return attachments
    # if function == 'addTenant':
    #     return 'tenantAdded'
