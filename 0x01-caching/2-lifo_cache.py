#!/usr/bin/env python3
"""
2-lifo_cache.py
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A last in, first out cache"""
    def __init__(self):
        """initializing"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item in the cache using LIFO"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.stack.remove(key)
            self.cache_data[key] = item
            self.stack.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.stack.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key, None)
