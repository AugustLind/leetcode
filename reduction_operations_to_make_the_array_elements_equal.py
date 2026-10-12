class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        nums.sort()
        operations = 0

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] != nums[i - 1]:
                operations += len(nums) - i

        return operations


sol = Solution()
num = sol.reductionOperations([5, 1, 3])
print(num)
