from dbAdapter import *

class templateAdapter(dbAdapter):
   
    def __init__(self, username,password,host,database):
        super(templateAdapter, self).__init__(username,password,host,database)
        self.dbName = 'template'
        self.clientIdentifierColumnName = 'Creator'

    def StoreTemplate(self,data, clientId):
        cursor = None
        try:
            exist = 0
            cursor = self.connection.cursor()
            args = (data['name'], data['description'], data['templateText'], data['createDate'], data['creator'])
            result_args = cursor.callproc('uspAddTemplate',args)
            self.connection.commit()

        except Exception, e:
            #log this failure
            print "StoreTemplate StoreTemplate: " + str(e)
            return False
        finally:
            if cursor != None:
                cursor.close()

    def ListAvaliableTemplates(self, clientId):
        query = "SELECT  Name, Description, TemplateText from Template where Creator = '{0}';".format(clientId)
        return self.simpleQueryRunner(query)

    def GetTemplate(self,data, tempalteId):
        query = "SELECT  Name, Description, TemplateText from Template where TemplateId = '{0}';".format(tempalteId)
        return self.simpleQueryRunner(query)
 
