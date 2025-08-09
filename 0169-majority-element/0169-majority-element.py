class Solution:
  def majorityElement(self, nums: list[int]) -> int:
    vote,c=0,nums[0]
    for i in nums:
        if vote==0:
            c=i
        if c==i:
            vote+=1
        else:
            vote-=1
    return c

    
        