class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        best = 0
        length = 1
        distinct = 1

        for i in range(1, len(word)):
            if word[i] >= word[i - 1]:
                length += 1
                if word[i] > word[i - 1]:
                    distinct += 1
            else:
                length = 1
                distinct = 1

            if distinct == 5:
                best = max(best, length)

        return best


sol = Solution()
val = sol.longestBeautifulSubstring("aeeeiiiioooauuuaeiou")
print(val)
