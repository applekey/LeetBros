from db.adapters.billAdapter import *
from db.adapters.userAdapter import *
from db.adapters.templateAdapter import *
from db.dbManager import *

import re
class templateEngine:
	

    def replace(self, text, clientId):

        usrAdapter =userAdapter(*dbManager.getDBConfig()) 
        billAdap = billAdapter(*dbManager.getDBConfig())
        tAdapter = templateAdapter(*dbManager.getDBConfig())

        splitText = text.split()
        print splitText

        for text in splitText:
            uFind = text.find('$user')
            bFind = text.find('$bill')
            tFind = text.find('$template')
            subText =''
            if uFind != -1:
                subText = text[uFind+len('$user'):]
            elif bFind != -1:
                subText = text[uFind+len('$user'):]
            elif tFind != -1:
                subText = text[uFind+len('$user'):]

            print subText

              


