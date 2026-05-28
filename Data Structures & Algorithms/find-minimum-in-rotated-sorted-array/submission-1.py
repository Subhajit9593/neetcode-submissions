class Solution:
    def findMin(self, nums: List[int]) -> int:
        s,e=0,len(nums)-1
        m=0
        while s<=e:
            m=(e+s)//2
            if nums[m]<nums[e]:
                if nums[m-1]<=nums[m]:
                    e=m-1
                else:
                    return nums[m]
            else:
                s=m+1


        return nums[m]