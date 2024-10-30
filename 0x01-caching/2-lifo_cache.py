#!/usr/bin/env python3

"""Lifo caching oparations.
"""

from collections import OrderedDict
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the LIFO cache and call parent init"""
        super().__init__()  # Call the parent class's __init__ method
        self.cache_data = OrderedDict()  # Use OrderedDict to maintain the order

    def put(self, key, item):
        """Assign item into self.cache_data with key"""
        if key is not None and item is not None:  # Check for None
            if key in self.cache_data:
                # If the key already exists, simply update it
                self.cache_data[key] = item
                return

            if len(self.cache_data) >= self.MAX_ITEMS:
                # If cache is full, discard the last item (LIFO)
                last_key, _ = self.cache_data.popitem()  # Pop the last item (LIFO)
                print(f"DISCARD: {last_key}")  # Print discarded key

            self.cache_data[key] = item  # Assign the item to the key

    def get(self, key):
        """Return the value linked to key in self.cache_data"""
        if key is None or key not in self.cache_data:  # Check for None or non-existent key
            return None
        return self.cache_data[key]  # Return the item

    def print_cache(self):
        """Print the current cache data"""
        print("Current Cache Data:")
        for key, value in self.cache_data.items():
            print(f"{key}: {value}")

