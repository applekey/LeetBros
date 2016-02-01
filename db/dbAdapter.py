import mysql.connector

class dbAdapter:
    # config = {
    #   'user': 'scott',
    #   'password': 'tiger',
    #   'host': '127.0.0.1',
    #   'database': 'employees',
    #   'raise_on_warnings': True,
    # }
    def __init__(self, username,password,host,database):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(user=self.username, password=self.password,
                              host=self.host,
                              database=self.database)
                              #connector.connect(**config)

    def simpleQueryRunner(self, query):
        result = []
        cursor = self.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        while row is not None:
            result.append(dict(zip(cursor.column_names, row)))
            row = cursor.fetchone()
        cursor.close()
        return result


    def disconnect(self):
        self.connection.close()
