class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e=0,len(nums)-1
        m=0
        while s<=e:
            m=(e+s)//2
            if nums[m]<nums[e]:
                e=m
            else:
                s=m+1


        return nums[m]