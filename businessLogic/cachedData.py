from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

class cachedData:
	def __init__(dataFile = './Beaker/tmp/cache/data', lockFile = './Beaker/tmp/cache/lock'):
		cache_opts = {
     	'cache.type': 'file',
     	'cache.data_dir': dataFile,
     	'cache.lock_dir': lockFile}
     	

	def createCacheFile():
        cache = CacheManager(**parse_cache_config_options(cache_opts))
		tmpl_cache = cache.get_cache('mytemplate', type='file', expire=5)

	def deleteCacheFile():
		## clean up
		pass
