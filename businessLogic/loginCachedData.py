#import * from cachedData
from dbManager import *
import uuid;
from datetime import datetime, date
from dbAdapter import *

class loginCachedData(dbAdapter):
	
	def getClientId(self,sid): 
		cursor = None
		try:
			cursor = self.connection.cursor()
			#print sid
			args = (str(sid),'')
			
			output = cursor.callproc('uspGETUserId',args)
			# output =cursor.execute('SELECT @ouserId')
			#results = cursor.fetchall()
			return output[1]
			#print results

		except Exception, e:
			#log this failure
			print "getClientId: " + str(e)
			return False
		finally:
			if cursor != None:
			    cursor.close()

	def setSID(self, sid, clientId):
	#invalidate cache
		sid = str(sid)
		clientId = str(clientId)
		query = "Insert into ClientSID (UserId, SID) values ('{0}','{1}');".format(clientId,sid)
		self.simpleQueryRunner(query)
		self.connection.commit()
		print query
		return None
