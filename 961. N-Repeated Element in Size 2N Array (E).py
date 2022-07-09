You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        
        nums.sort()
        
        for i in range(len(nums)-1):
            cnt = 1
            j= i+1
            while j < len(nums) and cnt <= len(nums)/2:
                if nums[j] == nums[i]:
                    cnt = cnt+1
                    j = j+1
                else:
                    j = len(nums)    
                if cnt == len(nums)/2:
                    return nums[i]
                    
        return nums[0]
            
            
   class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        
        return int((sum(nums)-sum(set(nums)))/(len(nums)/2-1))

        