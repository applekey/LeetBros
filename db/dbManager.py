import os
class dbManager:
    @staticmethod
    def getDBConfig():
        if 'shek' in os.getcwd():
            username = 'shek'
            password = ''
            host = "127.0.0.1"
            database = 'shayak'
        elif 'LeetBros' in os.getcwd():
            username = 'root'
            password = 'password'
            host = "127.0.0.1"
            database = 'housing'
        else:
            username = 'applekey'
            password = 'vancouver!@#'
            host = "applekey.mysql.pythonanywhere-services.com"
            database = 'applekey$housing'

        return (username,password,host,database)
