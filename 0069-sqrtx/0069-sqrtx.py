class Solution:
    def mySqrt(self, x: int) -> int:
        s,e=1,x
        while s<=e:
            m=(s+e)//2
            if m*m==x:
                return m
            elif m*m<x:
                s=m+1
            else:
                e=m-1
        return e