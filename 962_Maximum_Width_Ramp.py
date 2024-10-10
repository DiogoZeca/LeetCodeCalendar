# A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.
# Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        stack = []
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                ans = max(ans, j - stack.pop())
        return ans
    
    