#!/usr/bin/env python3

"""
This module provides support for type hint
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    "Calculate the start index for the given page"
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return(start_index, end_index)
