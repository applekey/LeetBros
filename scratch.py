from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options
import sched, time
from datetime import datetime


@cache.cache('gophers', expire=3600)
def get_results():
    # do something to retrieve data
    print 'hey'
    data = datetime.now()
    return data

@cache.cache('hank', expire=3600)
def get_results2():
    return 'askdjfla;j'

s = sched.scheduler(time.time, time.sleep)
def get_time(sc):     
    results = get_results()
    results2 = get_results2()
    print results,results2
    sc.enter(1, 1, get_time, (sc,))

print get_results()
print get_results()
print get_results()