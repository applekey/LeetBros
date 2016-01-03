import email,imaplib
import json
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
            self.imapSession = None
            print 'disconnected'
        except :
            print 'could not disconnect.'

    def listAttachments(self):
        if self.imapSession == None:
            print 'no session defined'
            return
        self.imapSession.select('[Gmail]/All Mail')

        typ, data = self.imapSession.search(None, '(SUBJECT "bill")')
        if typ != 'OK':
            print 'Error searching Inbox.'
            raise
        attachments = []
        # Iterating over all emails
        for msgId in data[0].split():
            typ, messageParts = self.imapSession.fetch(msgId, '(RFC822)')
            if typ != 'OK':
                print 'Error fetching mail.'
                raise

            emailBody = messageParts[0][1]

            mail = email.message_from_string(emailBody)
            for part in mail.walk():
                if part.get_content_maintype() == 'multipart':
                    # print part.as_string()
                    continue
                if part.get('Content-Disposition') is None:
                    # print part.as_string()
                    continue
                fileName = part.get_filename()

                if bool(fileName):
                    attachments.append(fileName)
        self.imapSession.close()
        print attachments
        if len(attachments) > 0:
            return json.dumps(attachments)
        else:
            return None
