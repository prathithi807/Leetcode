class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in s:
            if(i not in count):
                count[i]=1
            else:
                count[i]+=1
        for idx,ch in  enumerate(s):
            if(count[ch]==1):
                return idx
        return -1




              