import os,sys

emailDir = os.path.join(os.getcwd(),'attachments')
sys.path.append(emailDir)

from engine import *

engine = Engine()

engine.Run()