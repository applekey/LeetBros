CLIENT_ID = "197189255793-bl78f1gs26vel4ddt228prhu2156t60s.apps.googleusercontent.com"
#client secret: ObtDR11JgZpCBM30nylNC97h

from bottle import request

import uuid

from bottle import redirect
from oauth2client import client, crypt

from dbManager import *
from userAdapter import *
from include import *

def checkIfUserExists(clientId):
    return True
    (username,password,host,database) = dbManager.getDBConfig()

    userExist = False
    usrAdapter =userAdapter(username,password,host,database)
    usrAdapter.connect()
    userExist = usrAdapter.queryUser(username,password)
    usrAdapter.disconnect()
    return userExist


def updateuser(clientid):
    (username,password,host,database) = dbManager.getDBConfig()

    userExist = False
    usrAdapter =userAdapter(username,password,host,database)
    usrAdapter.connect()
    userExist = usrAdapter.queryUser(username,password)
    usrAdapter.disconnect()
    return userExist

def GetCurrentUserId():
    session = request.environ['beaker.session']
    
    sid = session['sessionId']
    print sid
    clientId = loginCachedData.getClientId(sid)
    print clientId
    return clientId
    ## implement this
    #return '76af103c-ea3e-11e5-a609-f7c4ee5bfee6'

def authenticate(request, response):

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
        name = request.forms.get('name')

        print 'name is' + str(name)

        if(str(name).strip() == 'demoName'):
            print 'demo user login'
            sid = uuid.uuid4().urn[9:]
            session = request.environ['beaker.session']
            session['sessionId'] = sid
            session.save()
            
            print sid

            loginCachedData.setSID(sid,uuid.UUID('204de18f-ed4f-11e5-8824-8c89a5c59145'))

            response.set_cookie('sessionId', sid)
            response.status = 200
            return 1


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
            userExist = checkIfUserExists(clientid) # add user to DB if new

            if not userExist:
                print 'user not exist'
                response.status = 400
                response.content_type = 'application/json'

                ## todo proper error
                response.body = json.dumps({'error': 'Object already exists with that name'})
                return 1
            else:
                print 'user exist'
                session = request.environ['beaker.session']
                session['sessionId'] = sid
                session.save()

                loginCachedData.setSID(sid,clientid)

                response.set_cookie('sessionId', sid)
                response.status = 200
                print 'set cookie'
                return 1
    return 0