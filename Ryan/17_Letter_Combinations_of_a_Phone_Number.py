class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if len(digits)==0:
            return ans
        
        dgt2let = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        
        def backtrack(idx, curr_str):
            if idx==len(digits):
                ans.append("".join(curr_str))
                return
            for letter in dgt2let[digits[idx]]:
                curr_str.append(letter)
                backtrack(idx+1, curr_str)
                curr_str.pop(-1)
        
        backtrack(0,[])
        return ans
        