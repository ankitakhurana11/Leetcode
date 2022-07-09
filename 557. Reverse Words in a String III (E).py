Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"



class Solution:
    def reverseWords(self, s: str) -> str:
        
        l=s.split(' ')
        l2= []
        for i in range(len(l)):
            l2.append(l[i][::-1])
        
        return ' '.join(l2)

        

class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = ''
        s= s.split(' ')
        for i in range(len(s)):
            new_s = new_s + s[i][::-1]
            if i != len(s)-1:
                new_s = new_s + ' '   
        return new_s