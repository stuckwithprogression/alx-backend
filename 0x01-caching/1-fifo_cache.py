#!/usr/bin/env/python3
"""
1-fifo_cache.py
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ a first in first out cache"""
    def __init__(self):
        """initializing"""
        super().__init__()
        self.order = []  # List to keep track of the order of keys for FIFO

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        if key not in self.cache_data and \
                len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the first item in the cache_data according to FIFO
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

        if key in self.cache_data:
            # Remove the key from the order list to update its position
            self.order.remove(key)

        # Add the item to cache_data and update the order list
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
