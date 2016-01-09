import mysql.connector

class dbAdapter:
    # config = {
    #   'user': 'scott',
    #   'password': 'tiger',
    #   'host': '127.0.0.1',
    #   'database': 'employees',
    #   'raise_on_warnings': True,
    # }
    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(user=self.username, password=self.password,
                              host='127.0.0.1',
                              database='housing')
                              #connector.connect(**config)
    def querry(self,querry, vars):
        raise Exception('Not implemented')
# cursor.execute(query, (hire_start, hire_end))
#
# for (first_name, last_name, hire_date) in cursor:
#   print("{}, {} was hired on {:%d %b %Y}".format(
#     last_name, first_name, hire_date))
#     cursor.close()

    def disconnect(self):
        self.connect.close()
