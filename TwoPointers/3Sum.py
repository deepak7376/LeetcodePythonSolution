from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    res = set()
    n = len(nums)        
    nums.sort()
    
    for i in range(n-2):     
        l, r = i+1, n-1
        while l<r:
            twoSum = nums[l]+nums[r]
            if twoSum==-nums[i]:
                res.add((nums[i], nums[l], nums[r]))
                l+=1
                r-=1
            elif twoSum<-nums[i]:
                l+=1          
            else:
                r-=1
            
    return res

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    n = 5
    for num in range(n-1, -1, -1):
        print(num)
    # print(threeSum(nums))