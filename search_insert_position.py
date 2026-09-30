class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return self.search(nums, target, 0, len(nums))

    def search(self, nums: list[int], target: int, lw: int, hg: int) -> int:
        if lw == hg:
            return lw

        middle = (hg + lw) // 2
        if nums[middle] <= target and nums[middle] >= target:
            return middle
        elif nums[middle] >= target:
            return self.search(nums, target, lw, middle)
        else:
            return self.search(nums, target, middle + 1, hg)
