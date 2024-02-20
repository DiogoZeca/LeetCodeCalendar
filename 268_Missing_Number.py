# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
    
    
    # [5, 4, 2, 0, 1]
    # n = 5
    # expected_sum = 5*6//2 = 15
    # actual_sum = 5+4+2+0+1 = 12
    # expected_sum - actual_sum = 15-12 = 3