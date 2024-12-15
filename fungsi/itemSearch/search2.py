import json
import math
import os

def option1(arr, size , search): # Linear Search
    for item in arr:
        if item.get(size) == search:
            return item
    return None
def option2(arr, size,low,high, search_value): # Binary Search
    while low <= high:
            mid = (low + high) // 2
            # membandingkan middle item size dengan search value
            if arr[mid].get(size) == search_value:
                return arr[mid]  # Item ditemukan
            elif arr[mid].get(size) < search_value:
                low = mid + 1  # Search di setengah kanan
            else:
                high = mid - 1  # Search di setengah kiri
    return None
def option3(arr ,new, searchValue):
    id_license = [arr['id'] for arr in arr]
    for item in arr:
        size = item.get(new)
    step = int(math.sqrt(size))  # Define jump size
    prev = 0
    
    # Jump through blocks until we find a block containing the target
    while id_license[min(step, size) - 1] < searchValue:
        prev = step
        step += int(math.sqrt(size))
        if prev >= size:
            return -1  # Target not found
    
    # Perform linear search in the identified block
    for i in range(prev, min(step, size)):
        if id_license[i] == searchValue:
            return arr[i]  # Target found
    
    return -1  # Target not found
