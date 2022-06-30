class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefix, postfix = 1, 1
        for i in range(0, n):
            res.append(prefix)
            prefix*=nums[i]
            
        for j in range(n-1, -1, -1):
            res[j]*=postfix
            postfix*=nums[j]
            
        return res
            
        