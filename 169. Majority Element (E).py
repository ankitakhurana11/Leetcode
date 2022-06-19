'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 
 '''

 class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic= {}
        for i, value in enumerate(nums):
            if value in dic.keys():
                dic[value] = dic[value]+1
                if dic[value] >float(len(nums)/2):
                    return value
            else:
                dic[value]= 1
                if dic[value] >float(len(nums)/2):
                    return value
        return None