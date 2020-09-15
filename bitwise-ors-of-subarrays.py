class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans =set()
        cur = set()
        
        for i in A:
            buff = set()
            
            buff.add(i)
            
            for j in cur:
                buff.add(i|j)
                
            cur = buff 
            ans.update(cur)
            
        return len(ans)