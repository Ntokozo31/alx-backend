#!/usr/bin/env python3

"""Lifo caching oparations.
"""

from collections import OrderedDict
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the LIFO cache and call parent init"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assign item into self.cache_data with key"""
       f key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

    def print_cache(self):
        """Print the current cache data"""
        print("Current Cache Data:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}") 
