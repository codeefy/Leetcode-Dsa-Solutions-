class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Early stopping
            if nums[i] > 0:
                break

            l, r = i + 1, n - 1

            while l < r:
                current = nums[i] + nums[l] + nums[r]

                if current == 0:
                    result.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif current < 0:
                    l += 1
                else:
                    r -= 1

        return result