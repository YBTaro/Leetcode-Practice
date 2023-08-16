# solution 1 : backtrack like DFS, but it's weird to say it's DFS because we don't travel the whole graph
# time: O(N*3^L), N is the number of cell in board, and L is the length of word
# space: O(1), if we igonre the input board. By the way, in the solution, i copy the board to use becuase i'll modify
# the board while backtracking and modify the original input is a disaster. -> O(board)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(row:int, col:int, suffix:str) -> bool:
            
            if len(suffix)==0:
                return True
            elif row < 0 or row == ROW or col < 0 or col == COL or Board[row][col]!=suffix[0]:
                return False
            
            Board[row][col] = "#" # means visited
            for row_offset, col_offset in ([1,0],[-1,0],[0,1],[0,-1]):
                if backtrack(row+row_offset, col+col_offset, suffix[1:]):
                    return True
            Board[row][col] = suffix[0]
            return False
        
        ROW = len(board)
        COL = len(board[0])
        Board = board.copy()
        # Modifying the input on a production code is a way to disaster. 
        # Amazon interviewers are strict on this. 
        
        for r in range(ROW):
            for c in range(COL):
                if backtrack(r,c,word):
                    return True
        return False
        
                
            
        