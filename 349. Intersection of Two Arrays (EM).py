Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    
        return list(set(nums1) & set(nums2))


        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        i, j = 0, 0
        match= []
        nums1.sort()
        nums2.sort()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                match.append(nums1[i])
                i = i+1
                j = j+1   
            elif j == len(nums2)-1:
                i = i+1
                j = 0
            else:
                j = j+1
            
        return set(match)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        res = []
        
        for i in nums1:
            if i in nums2:
                res.append(i)
        return set(res)
            

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        res = []
        
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res