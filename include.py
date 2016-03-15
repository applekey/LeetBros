import os, sys

attachmentDirectory = os.path.join(os.getcwd(),'attachments')
dbDirectory = os.path.join(os.getcwd(),'db')
sys.path.append(attachmentDirectory)
sys.path.append(dbDirectory)

adaptersDirectory = os.path.join(dbDirectory,'adapters')
sys.path.append(adaptersDirectory)

blDirectory = os.path.join(os.getcwd(),'businessLogic')
sys.path.append(blDirectory)

from dbManager import *
from userAdapter import *
from billAdapter import *
from loginCachedData import *
import AuthenticationManager


