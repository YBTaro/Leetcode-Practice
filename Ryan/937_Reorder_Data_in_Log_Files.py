# Solution - 1 - define sort
# Time: O(L*NlogN), L is the longest length of logs, N is the number of logs
# Space: O(L*N), L for keys and N for sort
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def get_key(log):
            _id, rest = log.split(" ",maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1,) #(1,None, None)
        return sorted(logs, key = get_key)
        