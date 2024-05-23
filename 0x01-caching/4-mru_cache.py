#!/usr/bin/env python3
"""
4-mru_cache.py
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """most recently used cache"""
    def __init__(self):
        """initializing"""
        super().__init__()
        # use OrderedDict() to main the order of insertion and access
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = next(reversed(self.cache_data))
            del self.cache_data[mru_key]
            print("DISCARD: {}".format(mru_key))

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        item = self.cache_data[key]
        del self.cache_data[key]
        self.cache_data[key] = item
        return item
