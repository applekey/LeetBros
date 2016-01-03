import email
import getpass, imaplib
import os
import sys

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

userName = 'applekeyhousing@gmail.com'
passwd = 'vancouver!@#'
print passwd


imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
typ, accountDetails = imapSession.login(userName, passwd)
if typ != 'OK':
    print 'Not able to sign in!'
    raise

imapSession.select('[Gmail]/All Mail')
typ, data = imapSession.search(None, 'ALL')
if typ != 'OK':
    print 'Error searching Inbox.'
    raise
print 'fdsa'
pass
# Iterating over all emails
for msgId in data[0].split():
    typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
    if typ != 'OK':
        print 'Error fetching mail.'
        raise

    emailBody = messageParts[0][1]
    print emailBody
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
            filePath = os.path.join(detach_dir, 'attachments', fileName)
            if not os.path.isfile(filePath) :
                print fileName
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
imapSession.close()
imapSession.logout()
