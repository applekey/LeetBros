from db.adapters.billAdapter import *
from db.adapters.userAdapter import *
from db.adapters.templateAdapter import *
from db.dbManager import *
import re

class templateEngine:
    def __scrubColumnName(self, attributeName):
        ## a func to do some addtional checking
        return attributeName

    def __handleUserAttributes(self, attributeName, clientId):
        usrAdapter =userAdapter(*dbManager.getDBConfig())
        usrAdapter.connect() 
        __scrubColumnName(attributeName)

        result = userAdapter.GetColumnValueIfExistsForClient(attributeName, clientId)
        ## get the data here?
        
        usrAdapter.disconnect()
        if not result:
            return None
        else:
            return result

    def __handleBillAttributes(self, attributeName):
        billAdap = billAdapter(*dbManager.getDBConfig())
        billAdap.connect()

        __scrubColumnName(attributeName)
        result = billAdap.GetColumnValueIfExistsForClient(attributeName, clientId)
        ## get the data here?
        
        billAdap.disconnect()
        if not result:
            return None
        else:
            return result

    def __handleTemplateAttributes(self, attributeName):
        tAdapter = templateAdapter(*dbManager.getDBConfig())
        tAdapter.connect()
        __scrubColumnName(attributeName)

        result = tAdapter.GetColumnValueIfExistsForClient(attributeName, clientId)
        ## get the data here?
        
        tAdapter.disconnect()
        if not result:
            return None
        else:
            return result


    def replace(self, text, clientId):

        newTxt = text
        splitText = text.split()
        smthToReplace = False

        for t in splitText:
            uFind = t.find('$user')
            bFind = t.find('$bill')
            tFind = t.find('$template')

            replacement = None

            if uFind != -1:
                subText = t[uFind+len('$user'):]
                replacement = __handleUserAttributes(subText)
            elif bFind != -1:
                subText = t[uFind+len('$user'):]
                replacement = __handleBillAttributes(subText)
            elif tFind != -1:
                subText = t[uFind+len('$user'):]
                replacement = __handleTemplateAttributes(subText)

            if replacement:
                ## replace the text, this is super inefficient and bad code
                ## me know, me clean up later
                newTxt.replace(t, replacement)
                smthToReplace = True

        if smthToReplace:
            return newTxt
        else:
            return None


