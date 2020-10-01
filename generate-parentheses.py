# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: 
            return ['']
        
        ans = []
        
        for par in range(n):
            for left in self.generateParenthesis(par):
                for right in self.generateParenthesis(n-par-1):
                    seq = '(',left,')', right
                    
                    ans.append(''.join(seq))
                    
        return ans