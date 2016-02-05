from bottle import route,static_file,post,request
import sys,os
import json
attachmentDirectory = os.path.join(os.getcwd(),'attachments')
dbDirectory = os.path.join(os.getcwd(),'db')
sys.path.append(attachmentDirectory)
sys.path.append(dbDirectory)

from emailAdapter import *
from peopleAdapter import *
from billAdapter import *
from owedAdapter import *
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

@route('/file/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='file/')

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

@route('/addBill', method='POST')
def addBill():

    print request.forms.get('peopleDropdown')

    data = {
        'name' : request.forms.get('name'),
        'desc' : request.forms.get('desc'),
        'amt' : request.forms.get('amount'),
        'date' : request.forms.get('duedate')
    }

    tenantemail = request.forms.get('peopleDropdown')

    # ## hack hack
    # data = request.forms.files.data
    # filename = data.filename
    # path = '/home/applekey/file'
    # fullPath = os.path.join(path,filename)
    # with open(fullPath,'w') as open_file:
    #     open_file.write(data.file.read())

    #TODO: USE CONNECTION POOLING

    (user, pw, host, db) = dbManager.getDBConfig()
    billAdap = billAdapter(user, pw, host, db)
    billAdap.connect()
    billId = billAdap.insertBill(data)
    billAdap.disconnect()

    pplAdapter = peopleAdapter(user, pw, host, db)
    pplAdapter.connect()
    personId = pplAdapter.queryClientByEmail(tenantemail)['people_id']
    pplAdapter.disconnect()

    owedAdap = owedAdapter(user, pw, host, db)
    owedAdap.connect()
    owedAdap.insertOwed(personId, billId)
    owedAdap.disconnect()

    return 'done'

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

    if function == 'viewBill':
        (username,password,host,database) = dbManager.getDBConfig()
        billAdap =billAdapter(username,password,host,database)

        billAdap.connect()
        results = billAdap.queryBills()
        billAdap.disconnect()

        print results

        return json.dumps(results)
