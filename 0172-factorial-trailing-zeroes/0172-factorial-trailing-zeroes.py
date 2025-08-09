class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum=0
        if n<5:
            return 0
        sum=0
        while n>=5:
            n=n//5
            sum+=n
        return sum



        
        