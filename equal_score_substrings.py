class Solution:
    def scoreBalance(self, s: str) -> bool:
        if not s:
            return False

        prefix_sum = [ord(s[0]) - ord("a") + 1]

        for i in range(1, len(s)):
            char_score = ord(s[i]) - ord("a") + 1
            prefix_sum.append(char_score + prefix_sum[i - 1])

        for num in prefix_sum:
            if num * 2 == prefix_sum[-1]:
                return True

        return False


sol = Solution()
res = sol.scoreBalance("bace")
print(res)
