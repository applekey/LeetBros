#import * from cachedData

loginDataCache = {} ##sid to client id matching

class loginCachedData:#(cachedData):

	#@cache.cache('getClientId', expire=3600)
	@staticmethod
	def getClientId(sid): 
		if sid in loginDataCache.keys():
			return loginDataCache[sid]
		else:
			return None

	@staticmethod
	def setSID(sid, clientId):
		#invalidate cache
		loginDataCache[sid] = clientId
		#cache.invalidate(get_results, 'getClientId', sid)

