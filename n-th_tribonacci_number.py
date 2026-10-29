class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1

        nums = [0, 0, 1]

        for i in range(n - 1):
            nums.append(nums[i] + nums[i + 1] + nums[i + 2])

        return nums[-1]


sol = Solution()
ans = sol.tribonacci(25)
print(ans)
