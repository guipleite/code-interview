# https://leetcode.com/problems/special-binary-string/submissions/

class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        
        count = 0
        i = 0
        res = []
        
        for j, k in enumerate(S):
            
            if k == '1':
                count+=1
            else:
                count-=1
            
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
              
        ans = ''.join(sorted(res)[::-1])
        
        return ans