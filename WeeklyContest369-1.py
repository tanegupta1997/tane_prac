"""
2917. Find the K-or of an Array
You are given a 0-indexed integer array nums, and an integer k.

The K-or of nums is a non-negative integer that satisfies the following:

The ith bit is set in the K-or if and only if there are at least k elements of nums in which bit i is set.
Return the K-or of nums.

Note that a bit i is set in x if (2i AND x) == 2i, where AND is the bitwise AND operator.
"""

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        arr = [""] * len(nums)
        for i in range(len(nums)):
            arr[i] = bin(nums[i])[2:]
            
        newstr = ""
        index = 0
        maxindex = 0
        for i in range(len(arr)):
            maxindex = max(len(arr[i]) - 1, maxindex)
        
        l = [0] * (maxindex+1)
        # print(arr)
        for i in range(len(arr)):
            for j in range(len(arr[i]) - 1, -1, -1):
                if arr[i][j] == "1":
                    l[len(arr[i]) -j - 1] += 1
        # l = l[::-1]
        # print(l)
        res = 0
        for i in range(len(l)):
            if l[i] >= k:
                res += pow(2, i)
        return res