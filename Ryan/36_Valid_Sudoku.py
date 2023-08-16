# solution 1
# Time: O(r*c) -> O(9*9)
# Space: O(9*9*3)

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		row_set = collections.defaultdict(set)
		col_set = collections.defaultdict(set)
		block_set = collections.defaultdict(set)

		for r in range(len(board)):
			for c in range(len(board[0])):
				if board[r][c].isdigit():
					s = board[r][c]
					block = (r//3, c//3)
					if s in row_set[r] or s in col_set[c] or s in block_set[block]:
						return False
					else:
						row_set[r].add(s)
						col_set[c].add(s)
						block_set[block].add(s)
		return True