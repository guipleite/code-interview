# LEetcode # 318 
# https://leetcode.com/problems/maximum-product-of-word-lengths/submissions/

# Brute force attempt
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxLen = 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                word1 = words[i]
                word2 = words[j]

                if self.checkChars(word1,word2):
                    lenght = len(word1)*len(word2)
                    
                    if lenght>maxLen:
                       maxLen = lenght
                    
        return maxLen
    
    
    def checkChars(self,word1,word2):
        
        L1 = list(word1)
        L2 = list(word2)
        
        for i in range(len(L1)):
            for j in range(len(L2)):
                if L1[i] == L2[j]:
                    return False
                
        return True

# Checks if lenght is greater before checking for repeated char

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        maxLen = 0
        
        for i in range(len(words)):
            for j in range(len(words)):
                word1 = words[i]
                word2 = words[j]
                
                lenght = len(word1)*len(word2)
                if lenght>maxLen:
                    if self.checkChars(word1,word2):
                    
                       maxLen = lenght
                    
        return maxLen
    
    
    def checkChars(self,word1,word2):
        
        L1 = list(word1)
        L2 = list(word2)
        
        for i in range(len(L1)):
            for j in range(len(L2)):
                if L1[i] == L2[j]:
                    return False
                
        return True

