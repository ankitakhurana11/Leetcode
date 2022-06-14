'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

 
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        nums= sorted(nums)
        i = 0

        while i < len(nums)-2:
            if nums[i]!= nums[i+1] and nums[i+1] != nums[i+2]:
                return nums[i+1]
            else:
                i = i+1
       
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        return nums[len(nums)-1]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res= 0 
        
        for n in nums:
            res = n ^ res # ^ represent XOR command
        return res


    
    
    
