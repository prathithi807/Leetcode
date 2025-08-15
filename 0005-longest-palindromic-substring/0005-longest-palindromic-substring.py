class Solution:
    def longestPalindrome(self, s: str) -> str:
        m=0
        for i in range(len(s)):
            r,l=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if m<(r-l+1):
                    m=r-l+1
                    right=r
                    left=l
                r+=1
                l-=1
            r,l=i+1,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if m<(r-l+1):
                    m=r-l+1
                    right=r
                    left=l
                r+=1
                l-=1
        return s[left:right+1]
        