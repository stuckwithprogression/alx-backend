#!/usr/bin/env python3
"""
a basic ditionary cache
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """a basic cache class"""
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None:
            return None
        return self.cache_data.get(key, None)
