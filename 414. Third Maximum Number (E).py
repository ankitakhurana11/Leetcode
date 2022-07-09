'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 
Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        nums= sorted(nums, reverse = True)       
        new_list = []
        for n in nums:
            if n in new_list:
                pass
            else:
                new_list.append(n)
        if len(new_list)> 2:
            return new_list[2]
        else:
            return new_list[0]
        
class Solution:
    def thirdMax(self, nums: List[int]) -> int:      
        if len(set(nums)) <=2:
            return max(nums)
        
        nums.sort(reverse = True)          
        cnt= 0
        for i in range(len(nums)):
            if nums[i] != nums[i+1]:
                cnt= cnt+1
                if cnt ==2:
                    return nums[i+1]
                    class Solution(object):
    def thirdMax(self, nums):
        v = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num not in v:
                if num > v[0]:   
                    v = [num, v[0], v[1]]
                elif num > v[1]: 
                    v = [v[0], num, v[1]]
                elif num > v[2]: 
                    v = [v[0], v[1], num]
        return max(nums) if float('-inf') in v else v[2]

