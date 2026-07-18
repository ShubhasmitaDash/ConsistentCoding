class Solution(object):
    def rob(self, nums):
        n=len(nums)
        if n==1:
            return nums[0]
        return max(self.rob1(nums[:-1]),self.rob1(nums[1:]))
    def rob1(self,nums):
        n=len(nums)
        if n==1:
            return nums[0]
        prev2=nums[0]
        prev1=max(nums[0], nums[1])
        for i in range(2,n):
            curr=max(prev1, nums[i]+prev2)
            prev2=prev1
            prev1=curr
        return prev1
        

        