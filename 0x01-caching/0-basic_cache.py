#!/usr/bin/env python3


class BaseCaching:
    def __init__(self):
        self.cache_data = {}

class BasicCache(BaseCaching):
    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return  # Do nothing if either key or item is None
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or doesn't exist
        return self.cache_data[key]

    def print_cache(self):
        """Print the current contents of the cache."""
        print("Current cache:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")
