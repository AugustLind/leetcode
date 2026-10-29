class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums) + 1):
            nums[i] = nums[i] + nums[i - 1]
        return nums


sol = Solution()
ans = sol.runningSum([3, 1, 2, 10, 1])
print(ans)
