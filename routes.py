from bottle import route,static_file,post,request,response, hook, redirect
import sys,os
import json

from include import *


@hook('before_request')
def authenticate():
    result = AuthenticationManager.doLogin(request, response)
    if result == 1:
        print 'returning ' + response.status
    
    print 'continuing ' + response.status

@route('/', method='GET')
def slashget():
    if response.status_code == 401:
        redirect('/login')
    else:
        redirect('/start')
    
@route('/', method='POST')
def slash():
    if response.status_code != 200:
        print '{0}: return before slash'.format(response.status_code)
        return response
    print 'sending to start'
    redirect('/start')

@route('/login')
@route('/login/')
def login():
    response.status = 200
    return static_file('login.html', root='static/html')

@route('/register')
def register():
    response.status = 200
    return static_file('register.html', root='static/html')

@route('/register', method='POST')
def registerUser():
    result = AuthenticationManager.doRegister(request, response)

    print 'result is: '
    print result
    if result:
        response.status = 200

@route('/start',  method='GET')
@route('/start', method='POST')
def start():
    if response.status != 200:
        print 'return before start'
        return response
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

@route('/addTemplate', method='POST')
def addTempalte():
    currentUserId = AuthenticationManager.GetCurrentUserId()
    data = {
        'name' : request.forms.get('templateName'),
        'description' : request.forms.get('templateDescription'),
        'templateText' : request.forms.get('templateText'),
        'createDate' : str(datetime.now()),
        'creator': currentUserId
    }

    tAdapter = templateAdapter(*dbManager.getDBConfig())
    tAdapter.connect()
    
    result = tAdapter.StoreTemplate(data, currentUserId) 

    tAdapter.disconnect()

@route('/addTenant', method='POST')
def addTenant():

    ###########################################
    # Note: this is used when a landlord adds a 
    # tenant, not a tenant adds themselves....
    #
    ###########################################
    currentUserId = AuthenticationManager.GetCurrentUserId()


    tenantName = request.forms.get('tenantName')
    tenantEmail = request.forms.get('tenantEmail')

    data = {
        'email' : tenantEmail,
        'loginName' : 'defaultLoginName',
        'passord' : 'defaultPassword',
        'firstName' : tenantName,
        'lastName': 'defualtLastName' ,
        'groupId': currentUserId ,
        'userType': 2 # 2 is phantom id
    }

    usrAdapter =userAdapter(*dbManager.getDBConfig())
    usrAdapter.connect()
    successCreate = usrAdapter.insertUser(data)
    usrAdapter.disconnect()

    return '<a href="/">Back</a>'
    # if successCreate == True:
    #     return 'Done'
    # else:
    #     return 'Error'

@route('/addBill', method='POST')
def addBill():
    currentUserId = AuthenticationManager.GetCurrentUserId()

    data = {
        'Name' : request.forms.get('name'),
        'Description' : request.forms.get('desc'),
        'Amount' : request.forms.get('amount'),
        'DueDate' : request.forms.get('duedate'),
        'BillIssuerId': currentUserId ,
        'BillPayeeId': currentUserId,
        'Paid' : False,
        'PaidDate': str(datetime.now()),
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

    billAdap = billAdapter(*dbManager.getDBConfig())
    billAdap.connect()
    billId = billAdap.insertBill(data)
    billAdap.disconnect()

    # pplAdapter = peopleAdapter(user, pw, host, db)
    # pplAdapter.connect()
    # personId = pplAdapter.queryClientByEmail(tenantemail)['people_id']
    # pplAdapter.disconnect()

    # owedAdap = owedAdapter(user, pw, host, db)
    # owedAdap.connect()
    # owedAdap.insertOwed(personIdc, billId)
    # owedAdap.disconnect()

    return '<a href="/">Back</a>'

@route('/functions/<function>')
def server_static(function):
    # if function == 'attachments':
    #     emailad = emailAdapter('applekeyhousing@gmail.com','vancouver!@#')
    #     emailad.connect()
    #     attachments = emailad.listAttachments()
    #     emailad.disconnect()
    #     return attachments
    clientId = AuthenticationManager.GetCurrentUserId()

    if function == 'loadViewTemplates':
        tAdapter = templateAdapter(*dbManager.getDBConfig())
        tAdapter.connect()
        result = tAdapter.ListAvaliableTemplates(clientId) 

        tAdapter.disconnect()
        return json.dumps(result)

    if function == 'upCommingBills':
        bAdapter = billAdapter(*dbManager.getDBConfig())
        bAdapter.connect()
        #bAdapter.insertBill(data)
        result = bAdapter.querryUpCommingBills(clientId)
        bAdapter.disconnect()
        return json.dumps(result)


    if function == 'recentlyPaidBill':
        bAdapter = billAdapter(*dbManager.getDBConfig())
        bAdapter.connect()
        #bAdapter.insertBill(data)
        result = bAdapter.querryPastDueBills(clientId)
        bAdapter.disconnect()
        return json.dumps(result)


    if function == 'viewTenants':
        usrAdapter =userAdapter(*dbManager.getDBConfig())

        usrAdapter.connect()
        results = usrAdapter.queryUserByClientId(clientId)
        usrAdapter.disconnect()
        return json.dumps(results)

    if function == 'viewBill':
        billAdap =billAdapter(*dbManager.getDBConfig())

        billAdap.connect()
        results = billAdap.queryBills(clientId)
        billAdap.disconnect()

        return json.dumps(results)