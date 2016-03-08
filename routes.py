from bottle import route,static_file,post,request,response, hook, redirect
import sys,os
import json

from include import *

@hook('before_request')
def authenticate():
    result = AuthenticationManager.authenticate(request, response)
    if result == 1:
        return response
    print 'continuing'

@route('/', method='GET')
@route('/', method='POST')
def slash():
    print request.cookies.keys()
    print 'sending to start'
    redirect('/start')

@route('/login')
@route('/login/')
def login():
    response.status = 200
    return static_file('login.html', root='static/html')

@route('/start',  method='GET')
def start():
    return static_file('start.html', root='static/html')

@route('/shtml/<filename>')
def server_static(filename):
    return static_file(filename, root='static/html')

@route('/js/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/js/')

@route('/files/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='files/')

@route('/template/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/startbootstrap-sb-admin-2-gh-pages/')

@route('/addTenant', method='POST')
def addTenant():
    session = request.environ['beaker.session']
    print session['sessionId']

    tenantName = request.forms.get('tenantName')
    tenantEmail = request.forms.get('tenantEmail')
    #create container for db entry
    container = peopleContainer((tenantName)
                                ,(tenantEmail))

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

    data = {
        'name' : request.forms.get('name'),
        'desc' : request.forms.get('desc'),
        'amt' : request.forms.get('amount'),
        'date' : request.forms.get('duedate')
    }

    tenantemail = request.forms.get('peopleDropdown')

    ## hack hack
    for file in request.files:
        filObj = request.files[file]
        filename = filObj.filename
        path = './files'
        fullPath = os.path.join(path,filename)
        filObj.save(fullPath,overwrite=True)

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

        return json.dumps(results)

@route('/test')
def shit():
    response.body = "test"
    return response