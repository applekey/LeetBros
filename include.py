import os, sys

attachmentDirectory = os.path.join(os.getcwd(),'attachments')
dbDirectory = os.path.join(os.getcwd(),'db')
sys.path.append(attachmentDirectory)
sys.path.append(dbDirectory)

adaptersDirectory = os.path.join(dbDirectory,'adapters')
sys.path.append(adaptersDirectory)

from dbManager import *
from userAdapter import *
from billAdapter import *
import AuthenticationManager

# from emailAdapter import *
# from peopleAdapter import *

# from owedAdapter import *
# from peopleContainer import *



