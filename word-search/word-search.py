# https://leetcode.com/problems/word-search/submissions/

class Solution:
    def DFS(self,row, col, curr, board, word):
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == word[curr]: 
                temp = board[row][col]
                board[row][col] = '#'

                if curr == len(word)-1:
                    return True

                result = self.DFS(row-1, col, curr+1, board, word) or self.DFS(row+1, col, curr+1, board, word) or self.DFS(row, col-1, curr+1, board, word) or self.DFS(row, col+1, curr+1, board, word)

                board[row][col] = temp

                return result
            else:
                return False
       
    
    def exist(self, board: List[List[str]], word: str) -> bool:    

        for row in range(len(board)):
            for col in range(len(board[0])):

                check = self.DFS(row, col, 0, board, word)
                
                if check:
                    return True
                    
        return False
    