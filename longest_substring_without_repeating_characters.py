class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            return 2

        max_value = 0

        for i in range(len(s)):
            value = 0
            string_set = set()
            for j in range(i, len(s)):
                if s[j] in string_set:
                    break
                else:
                    string_set.add(s[j])
                    value += 1
            max_value = max(max_value, value)

        return max_value


sol = Solution()
val = sol.lengthOfLongestSubstring("mq3")

print(val)
