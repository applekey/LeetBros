from bottle import route,static_file,post,request,response, hook, redirect
from beaker.middleware import SessionMiddleware
from oauth2client import client, crypt
import sys,os,uuid
import json

CLIENT_ID = "197189255793-bl78f1gs26vel4ddt228prhu2156t60s.apps.googleusercontent.com"
#client secret: ObtDR11JgZpCBM30nylNC97h

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

def updateuser(clientid):
    pass

@hook('before_request')
def authenticate():
    usersid = None
    sid = None
    #response.headers['Access-Control-Allow-Origin'] = '*'
    #response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
    #response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

    if 'sessionId' in request.cookies.keys():
        usersid = request.cookies['sessionId']

    if 'sessionId' in request.environ['beaker.session']:
        sid = request.environ['beaker.session']['sessionId']

    if "/login" in request.path \
        or "/shtml/" in request.path \
        or "/template/" in request.path \
        or "/js/" in request.path \
        or "/functions" in request.path:
        print 'pass'
        pass
    elif (usersid is None or usersid != sid):
        token = request.forms.get('auth_token')
        if (token is None):
            print 'redirect to login'
            redirect('/login')
        else:
            idinfo = client.verify_id_token(token, CLIENT_ID)
            # If multiple clients access the backend server:
            # if idinfo['aud'] not in [ANDROID_CLIENT_ID, IOS_CLIENT_ID, WEB_CLIENT_ID]:
            #     raise oauth2client.crypt.AppIdentityError("Unrecognized client.")
            # if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            #     raise oauth2client.crypt.AppIdentityError("Wrong issuer.")
            # if idinfo['hd'] != APPS_DOMAIN_NAME:
            #     raise oauth2client.crypt.AppIdentityError("Wrong hosted domain.")

            clientid = idinfo['sub']
            sid = uuid.uuid4().urn[9:]
            updateuser(clientid) # add user to DB if new
            session = request.environ['beaker.session']
            session['sessionId'] = sid
            session.save()
            response.set_cookie('sessionId', sid)
            response.status = 200
            print 'set cookie'
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
def hello_world():
    return static_file('login.html', root='static/html')

@route('/start',  method='GET')
def hello_world():
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
