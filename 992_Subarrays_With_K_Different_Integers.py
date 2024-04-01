# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
#     For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        """
        count subarrays with at most K distinct elements. it makes problem much easier!
        goodLessEqualK(nums, k)-goodLessEqualK(nums, k-1)

        """
        def goodLessEqualK(nums, k):
            dist=0
            freq=[0]*20001
            cnt=0
            l=0
            n=len(nums)
            for r in range(n):
                x=nums[r]
                freq[x]+=1
                if freq[x]==1: dist+=1
                while dist>k:
                    y=nums[l]
                    freq[y]-=1
                    if freq[y]==0: dist-=1
                    l+=1
                cnt+=(r-l+1)
            return cnt
        
        if k==1: return goodLessEqualK(nums, k)
        else: return goodLessEqualK(nums, k)-goodLessEqualK(nums, k-1)
        
