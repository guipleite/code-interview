# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        close_open = {')':'(', ']':'[', '}':'{'}
        allowed = "([{"
        
        sz = len(s)
        
        if sz == 1:
            return False
        elif sz ==0:
            return True
       
        for i in range(sz):
            
            curr = s[i]
            
            if curr in allowed:
                stack.append(curr)
                
            else:
                if stack:
                    if stack[-1] == close_open[curr]:
                        stack.pop()
                        
                else:
                    return False
        
        return not stack
        