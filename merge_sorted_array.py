class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = 0
        p2 = 0
        result = []

        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                result.append(nums1[p1])
                p1 += 1
            else:
                result.append(nums2[p2])
                p2 += 1

        result.extend(nums1[p1:m])
        result.extend(nums2[p2:n])

        nums1[:] = result
