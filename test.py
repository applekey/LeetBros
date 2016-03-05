import sys,os,datetime
dbDirectory = os.path.join(os.getcwd(),'db')
emailDir = os.path.join(os.getcwd(),'attachments')
sys.path.append(dbDirectory)
sys.path.append(emailDir)

from peopleAdapter import *
from emailAdapter import *
from userAdapter import *
from engine import *


# username = 'applekey'
# password = 'vancouver!@#'
# host = "applekey.mysql.pythonanywhere-services.com"
# database = 'applekey$housing'

# username = 'shek'
# password = ''
# host = "127.0.0.1"
# database = 'shayak'

username = 'root'
password = 'password'
host = "127.0.0.1"
database = 'housing'

# engine = Engine()
# engine.Run()

adapter = userAdapter(username,password,host,database)
adapter.connect()
print adapter.queryUser('abcf','fcdefdsfafdsaf')

# print adapter.queryBill()
# print adapter.queryOwed()
# print adapter.queryUnpaidBills()
adapter.disconnect()

#######
def createBillReminderMail():
    return {
        'email' : 'shayak007@gmail.com', 'title' : title, 'html': html
    }


data = { 'email': 'applekey@gmail.com', 'personname': 'shayak', 'billname': 'bill1',
'bill_link' : 'applekey.pythonanywhere.com', 'billdate': datetime.datetime.now()}

html="""\
        <html>
          <head></head>
            <body>
                <h1>HEY BUDDY</h1>
                <h2>
                    <a href="{0}" style="text-decoration:none">
                        PAY YOUR GOD DAMN BILL!
                    </a><br><br>
                </h2>
            </body>
        </html>
        """.format(data['bill_link'], data['personname'])
title = 'Reminder: {0} due on {1}'.format(data['billname'], data['billdate'])

#adapter = emailAdapter('dotaspider007@gmail.com', 'dotapass')
#adapter.sendHtmlMail(createBillReminderMail())
