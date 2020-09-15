class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <=1:
            return s
        
        row = 0
        fixed = ['']*(len(s))
        
        for i in range(len(s)):
            fixed[row]+=s[i]
            
            if row == numRows-1: 
                flag = False
                    
            elif row == 0: 
                flag = True
  
            if flag: 
                row += 1
            else: 
                row -= 1
                
        fixed = ''.join(fixed)
            
        return fixed
        
        