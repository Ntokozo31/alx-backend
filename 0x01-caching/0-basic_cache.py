#!/usr/bin/env python3


class BaseCaching:
    """BaseCaching defines a caching system"""
    def __init__(self):
        self.cache_data = {}


class BasicCache(BaseCaching):
    """BaseCaching class that inherit from BaseCaching"""

    def put(self, key, item):
        """Assign item into a dictionary self.cache_data with key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key in self.cache_data"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
