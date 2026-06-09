class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        sums=0
        for i in range (0,len(nums),2):
            sums+=nums[i]
        return sums
        