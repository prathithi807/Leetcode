class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ansarray = [0]*len(temperatures)
        stack = []
        

        for i in range(len(temperatures)):

            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ansarray[index] = (i - index)

            stack.append(i)
        
        return ansarray
            
        