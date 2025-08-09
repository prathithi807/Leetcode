class Solution:
    def SumOfDigits(num):
        summ = 0
        for i in str(num):
            summ += int(i)
        return summ

    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = Solution.SumOfDigits(num)
        return num



        