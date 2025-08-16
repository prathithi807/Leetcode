class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        for i in range(len(s)):
            seen = set()
            r, l = i, i
            while r < len(s) and s[r] not in seen:
                seen.add(s[r])
                if m < (r - l + 1):
                    m = r - l + 1
                r += 1
        return m
