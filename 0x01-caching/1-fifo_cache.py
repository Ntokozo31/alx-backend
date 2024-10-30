#!/usr/bin/env python3


class BaseCaching:
    """BaseCaching defines a caching system"""
    MAX_ITEMS = 4

    def __init__(self):
        self.cache_data = {}


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the FIFO cache and call parent init"""
        super().__init__()

    def put(self, key, item):
        """Assign item into self.cache_data with key"""
        if key is not None and item is not None:
            if key not in self.cache_data and len(
                    self.cache_data) >= self.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                del self.cache_data[first_key]

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
