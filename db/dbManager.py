import os
class dbManager:
    @staticmethod
    def getDBConfig():
        if 'LeetBros' in os.getcwd():
            username = 'root'
            password = 'password'
            host = "127.0.0.1"
            database = 'housing'
        elif 'shek' in os.getcwd():
            username = 'shek'
            password = ''
            host = "127.0.0.1"
            database = 'shayak'
        else:
            username = 'applekey'
            password = 'vancouver!@#'
            host = "applekey.mysql.pythonanywhere-services.com"
            database = 'applekey$housing'

        return (username,password,host,database)
