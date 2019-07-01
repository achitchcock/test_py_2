import redis
from pickle_test import build_data

class TiltCache(object):
    def __init__(self):
        self._cache = redis.Redis()
        self._cache_name = "tilt_cache"
        self._preexisting_tilts = self.check_existing()

    def check_existing(self):
        if self._cache.exists(self._cache_name):
            return self._cache.hgetall(self._cache_name)
        else:
            return None

    def store_tilts(self, tilt_data):
        for dn, tilt in tilt_data.iteritems():
            self._cache.hset(self._cache_name, dn, tilt)

    def get_tilt_for_dn(self, dn):
        try:
            return self._cache.hget(self._cache_name, dn)
        except:
            return None



tilt_data = build_data(100)
tc = TiltCache()
tc.store_tilts(tilt_data)
tc.get_tilt_for_dn('fake_dn')





