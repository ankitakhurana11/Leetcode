'''
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
 

Constraints:

1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
Accepted
96,241
Submissions
279,640
'''

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        l = 1
        r = 1
        typed_name = ''
        first = name[0]
        
        if name[0]!= typed[0]:
            return False
        
        while l < len(name) and r < len(typed):
            if name[l] == typed[r]:
                l= l+1
                r= r+1
                typed_name = typed_name + typed[r-1]
                first = name[l-1]
            elif typed[r]== first and typed[r] == typed[r-1]:
                r= r+1
            else:
                return False
        
        while typed_name != typed and r < len(typed):
            if typed[r] == typed[r-1]:
                r= r+1
            else:
                return False
            
        while l != len(name):
            return False
        
        return True

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i = i+1
                j = j+1
            elif j == 0 or typed[j] != typed[j-1]:
                return False
            else:
                j = j+1
        return i == len(name) 

        

class Solution:
    def isLongPressedName(self, name, typed):
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)

