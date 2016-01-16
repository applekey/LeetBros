import json
class peopleContainer:
    #this class contains the fields for clients
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __init__(self,dbResult):
        self.name = dbResult['people_name']
        self.email = dbResult['people_email']

    def seralizeToJson(self):
        newDict = self.__dict__
        newDict['people_name'] = self.__dict__.pop('name')
        newDict['people_email'] = self.__dict__.pop('email')
        return json.loads(json.dumps(newDict))


    @staticmethod
    def seralizeToJsonList(ilist):
        result = []
        for people in ilist:
            result.append (people.seralizeToJson())

        return result
