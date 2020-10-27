# https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        def backtrack(N,K):
            
            if N==1 and K == 1 :
                return 0    
            
            size = 2**(N-2)
            
            if K <= size:
                return backtrack(N-1,K)
        
            else:
                return 1-backtrack(N-1,K-size)
            
        return backtrack(N,K)