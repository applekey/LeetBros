from bottle import route,static_file,post,request
import sys,os
import json
attachmentDirectory = os.path.join(os.getcwd(),'attachments')
dbDirectory = os.path.join(os.getcwd(),'db')
sys.path.append(attachmentDirectory)
sys.path.append(dbDirectory)

from emailAdapter import *
from peopleAdapter import *
from peopleContainer import *
from dbManager import *

@route('/')
def hello_world():
    return static_file('login.html', root='static/html')

@route('/start',  method='POST')
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
def addTenant():
    print 'hererererre'
    tenantName = request.forms.get('tenantName')
    tenantEmail = request.forms.get('tenantEmail')
    #create container for db entry
    container = peopleContainer((tenantName)
                                ,(tenantEmail))

    print tenantName + tenantEmail

    (username,password,host,database) = dbManager.getDBConfig()

    pplAdapter =peopleAdapter(username,password,host,database)
    pplAdapter.connect()
    successCreate = pplAdapter.createClient(container)
    pplAdapter.disconnect()

    if successCreate == True:
        return 'Done'
    else:
        return 'Error'


@route('/functions/<function>')
def server_static(function):
    # if function == 'attachments':
    #     emailad = emailAdapter('applekeyhousing@gmail.com','vancouver!@#')
    #     emailad.connect()
    #     attachments = emailad.listAttachments()
    #     emailad.disconnect()
    #     return attachments
    if function == 'viewTenants':
        (username,password,host,database) = dbManager.getDBConfig()
        pplAdapter =peopleAdapter(username,password,host,database)

        pplAdapter.connect()
        results = pplAdapter.queryClients()
        pplAdapter.disconnect()

        return json.dumps(results)
