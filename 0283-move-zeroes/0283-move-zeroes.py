class Solution:
    def moveZeroes(self, nums):
        j = 0 # Pointer to place the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current element with the element at index j 
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 # Move j to the next index for placing non-zero
