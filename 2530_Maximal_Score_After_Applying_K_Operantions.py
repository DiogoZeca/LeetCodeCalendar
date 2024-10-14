# You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.
# In one operation:
#     choose an index i such that 0 <= i < nums.length,
#     increase your score by nums[i], and
#     replace nums[i] with ceil(nums[i] / 3).
# Return the maximum possible score you can attain after applying exactly k operations.
# The ceiling function ceil(val) is the least integer greater than or equal to val.


import math
import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Convert nums to a max-heap by pushing negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        while k > 0:
            # Pop the largest element (convert back to positive)
            largest = -heapq.heappop(max_heap)
            score += largest
            # Replace the element with ceil(largest / 3) and push back to heap
            heapq.heappush(max_heap, -math.ceil(largest / 3))
            k -= 1
        
        return score