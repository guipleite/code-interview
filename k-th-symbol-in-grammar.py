# https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        if N == 0 or N is None or K is None:
            return 0

        def backtrack(N,K):
            
            if N<=1 and K <= 1 :
                return 0    
            
            size = 2**(N-2)
            
            if K <= size:
                return backtrack(N-1,K)
        
            else:
                return 1-backtrack(N-1,K-size)
            
        return backtrack(N,K)