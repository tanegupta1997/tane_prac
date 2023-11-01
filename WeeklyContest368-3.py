"""
2910. Minimum Number of Groups to Create a Valid Assignment

You are given a 0-indexed integer array nums of length n.

We want to group the indices so for each index i in the range [0, n - 1], it is assigned to exactly one group.

A group assignment is valid if the following conditions hold:

For every group g, all indices i assigned to group g have the same value in nums.
For any two groups g1 and g2, the difference between the number of indices assigned to g1 and g2 should not exceed 1.
Return an integer denoting the minimum number of groups needed to create a valid group assignment.
"""
class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        
        
        m = collections.defaultdict(list)
        for i in range(len(nums)):
            m[nums[i]].append(i)
        n = []
        for key in m.keys():
            n.append(len(m[key]))
        n.sort()
        groups = 0
        
        @cache
        def rec2(num, g1):
            g2 = g1 + 1
            for x in range(0, num//g1 + 1, 1):
                if (num - g1 * x) % (g1 + 1) == 0:
                    return (x, (num - g1 * x) / (g1 + 1))
            return (-1, -1)
        
        mapp = []
        @cache
        def rec(g1):
            if (g1 <= 0):
                return
            tgroups = 0
            found = True
            for i in n:
                x, y = rec2(i, g1)
                if (x != -1 and y != -1):
                    tgroups += x
                    tgroups += y
                else:
                    found = False
                    break
            if found == True:
                heapq.heappush(mapp, tgroups)
                return
            else:
                rec(g1 - 1)
            
        rec(len(nums))
        return int(heapq.heappop(mapp))
