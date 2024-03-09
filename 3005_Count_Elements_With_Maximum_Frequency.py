# You are given an array nums consisting of positive integers.
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
# The frequency of an element is the number of occurrences of that element in the array.


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        max_freq_elements = []
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
            if freq_map[num] > max_freq:
                max_freq = freq_map[num]
                max_freq_elements = [num]
            elif freq_map[num] == max_freq:
                max_freq_elements.append(num)
        return max_freq_elements 
                
        




