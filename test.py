from include import *

## bill tests

user = 'root'
pw = 'password'
host = "127.0.0.1"
db = 'housing'

# (user, pw, host, db) = dbManager.getDBConfig()
print (user, pw, host, db)
userAdapter = userAdapter(user, pw, host, db)
userAdapter.connect()

data = {
        'email' : "gmail.fcom",
        'loginName' : "applekey",
        'passord' : "vancouver!@#",
        'firstName' : "Vincent",
        'lastName': "Chen",
        'userType': 3
    }

#userId = userAdapter.queryUser()

print userAdapter.insertUser(data)

userAdapter.disconnect()

