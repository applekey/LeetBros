import os, sys, datetime

rootDir = os.path.dirname(os.getcwd())

attachmentDirectory = os.path.join(rootDir,'attachments')
dbDirectory = os.path.join(rootDir,'db')
sys.path.append(attachmentDirectory)
sys.path.append(dbDirectory)

adaptersDirectory = os.path.join(dbDirectory,'adapters')
sys.path.append(adaptersDirectory)

blDirectory = os.path.join(rootDir,'businessLogic')
sys.path.append(blDirectory)

from outstanding import *
from dbManager import *
from userAdapter import *
from billAdapter import *
