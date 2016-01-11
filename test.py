import sys,os
dbDirectory = os.path.join(os.getcwd(),'db')
sys.path.append(dbDirectory)

from peopleAdapter import *

username = 'applekey'
password = 'vancouver!@#'
host = "applekey.mysql.pythonanywhere-services.com"
database = 'applekey$housing'

adapter = peopleAdapter(username,password,host,database)
adapter.connect()
print adapter.querryClients()
adapter.disconnect()
