"""
2908. Minimum Sum of Mountain Triplets I
You are given a 0-indexed array nums of integers.

A triplet of indices (i, j, k) is a mountain if:
i < j < k
nums[i] < nums[j] and nums[k] < nums[j]
Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.
"""
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        leftLowest = [0] * n
        rightLowest = [0] * n
        leftLowest[0] = (nums[0], 0)
        rightLowest[n - 1] = (nums[-1], n - 1)
        for i in range(1, n):
            tillNowLeft = leftLowest[i - 1][0]
            if (tillNowLeft > nums[i]):
                leftLowest[i] = (nums[i], i)
            else:
                leftLowest[i] = leftLowest[i - 1]
        for i in range(n - 2, -1 , -1):
            tillNowRight = rightLowest[i + 1][0]
            if (tillNowRight > nums[i]):
                rightLowest[i] = (nums[i], i)
            else:
                rightLowest[i] = (rightLowest[i + 1])
        poss = inf
        #print(leftLowest, rightLowest)
        for i in range(1, n - 1):
            curr = nums[i]
            leftNum, leftIndex = leftLowest[i]
            rightNum, rightIndex = rightLowest[i]
            if leftNum < curr and rightNum < curr and leftIndex < i and rightIndex > i:
                poss = min(poss, nums[leftIndex] + nums[i] + nums[rightIndex])
        if poss == inf:
            return -1
        else:
            return poss