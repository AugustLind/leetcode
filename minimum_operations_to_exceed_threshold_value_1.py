class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tot = 0
        for num in nums:
            if num < k:
                tot += 1
        return tot
