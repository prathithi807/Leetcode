class Solution:
    def findLHS(self, nums: List[int]) -> int:
        m=0
        d={}
        for i in nums:
            if i  in d:
                d[i]+=1
            else:
                d[i]=1
        for k in d:
            if k+1 in d and d[k]+d[k+1]>m:
                m=d[k]+d[k+1]
        return m


        