import sys,os,datetime
dbDirectory = os.path.join(os.getcwd(),'db')

sys.path.append(dbDirectory)

from peopleAdapter import *
from emailAdapter import *
from dbManager import *

class Engine:

    __emailAdapter = emailAdapter('will.reminder@gmail.com', 'vancouver!@#')

    def __init__(self):
        (username,password,host,database) = dbManager.getDBConfig()
        self.__pplAdapter = peopleAdapter(username,password,host,database)
        self.__pplAdapter.connect()

    def __del__(self):
        self.__pplAdapter.disconnect()

    def Run(self):
        # iterate through owed table and send emails
        bills = self.__pplAdapter.queryUnpaidBills()
        for bill in bills:
            params = {
                'bill_link': 'applekey.pythonanywhere.com',
                'personName': bill['personName']
            }

            data = {
                'title': 'Reminder: {0} due on {1}'.format(bill['billName'], bill['dueDate']),
                'email': bill['email'],
                'html': self.getEmailHtml(params)
            }
            self.__emailAdapter.sendHtmlMail(data)

    def getEmailHtml(self, data):
        return """\
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
        """.format(data['bill_link'], data['personName'])