import time
from threading import Lock

CACHE_TTL = 60  # seconds
_cache = {}
_cache_lock = Lock()

def get_cached(key, loader):
    """
    Return cached value if fresh; otherwise call loader(), cache it, and return.
    """
    now = time.time()
    with _cache_lock:
        if key in _cache:
            value, ts = _cache[key]
            if now - ts < CACHE_TTL:
                return value
        # Miss or expired: refresh
        value = loader()
        _cache[key] = (value, now)
        return value