class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        lp = 0
        rp = 1
        longest_pal = s[0]
        curr = s[0]

        while lp < len(s) - 1:
            curr += s[rp]
            if s[lp] == s[rp] and len(curr) > len(longest_pal) and curr == curr[::-1]:
                longest_pal = curr

            rp += 1
            if rp == len(s):
                lp += 1
                rp = lp + 1
                curr = s[lp]

        return longest_pal


sol = Solution()
print(sol.longestPalindrome("cbbd"))
