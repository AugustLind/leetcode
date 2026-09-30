class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:

        properties.sort(key=lambda p: (-p[0], p[1]))

        print(properties)

        tot = 0
        max_def = 0
        for _, d in properties:
            if d < max_def:
                tot += 1
            else:
                max_def = d
        return tot


sol = Solution()
value = sol.numberOfWeakCharacters([[7, 9], [10, 7], [6, 9], [10, 4], [7, 5], [7, 10]])

print(value)
