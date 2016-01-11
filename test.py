import sys,os
attachmentDirectory = os.path.join(os.getcwd(),'attachments')
sys.path.append(attachmentDirectory)

from dbAdater import *


adapter = dbAdapter()
