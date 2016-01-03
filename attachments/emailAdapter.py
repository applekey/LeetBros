import email,imaplib

class emailAdapter:
    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.imapSession = None

    def connect(self):
        try:
            self.imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
            typ, accountDetails = self.imapSession.login(self.username, self.password)
            if typ != 'OK':
                print 'Not able to sign in!'
                raise
            print 'connected'
        except :
            print 'could not connect.'

    def disconnect(self):
        try:
            #self.imapSession.close()
            self.imapSession.logout()
            print 'disconnected'
        except :
            print 'could not disconnect.'

    def listAttachments(self):
        pass
