# You are given an integer array nums and an integer k.
# The frequency of an element x is the number of times it occurs in an array.
# An array is called good if the frequency of each element in this array is less than or equal to k.
# Return the length of the longest good subarray of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        l, r = 0, 0
        freq = {}
        max_len = 0
        while r < n:
            freq[nums[r]] = freq.get(nums[r], 0) + 1
            while freq[nums[r]] > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len


