import emailAdapter
import sys,os,datetime
dbDirectory = os.path.join(os.getcwd(),'db')

sys.path.append(dbDirectory)

class Engine:

	def Run(self):
		# iterate through owed table and send emails