class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: 
            return ['']
        
        ans = []
        
        for c in range(n):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(n-1-c):
                    seq = '(',left,')', right
                    
                    ans.append(''.join(seq))
                    
        return ans