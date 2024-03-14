# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        prefix_sums = {0: 1}
        count = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - goal in prefix_sums:
                count += prefix_sums[prefix_sum - goal]
            if prefix_sum in prefix_sums:
                prefix_sums[prefix_sum] += 1
            else:
                prefix_sums[prefix_sum] = 1

        return count

