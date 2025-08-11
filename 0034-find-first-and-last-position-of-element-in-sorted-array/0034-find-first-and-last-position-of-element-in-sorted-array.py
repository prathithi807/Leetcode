class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[-1,-1]
        s,e=0,len(nums)-1
        while s<=e:
            m=(s+e)//2
            if nums[m]==target:
                result[0]=m
                e=m-1
            elif target<nums[m]:
                e=m-1
            else:
                s=m+1
        s,e=0,len(nums)-1
        while s<=e:
            m=(s+e)//2
            if target==nums[m]:
                result[1]=m
                s=m+1
            elif target<nums[m]:
                e=m-1
            else:
                s=m+1
        return result    

