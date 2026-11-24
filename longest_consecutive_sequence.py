class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        unique_nums = set(nums)
        max_len = 0

        for num in unique_nums:
            if num - 1 not in unique_nums:
                len = 1
                while num + len in unique_nums:
                    len += 1

                max_len = max(max_len, len)

        return max_len


sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
