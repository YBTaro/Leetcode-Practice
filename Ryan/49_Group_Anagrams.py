# solution 1: Categorize by Sorted String
# Time: O(K*N(log(N))), K is the size of inputs, N is the length of each input
# Space:O(NK), for ans
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #ans = []
        #dic = {}
        dic = collections.defaultdict(list)
        for s in strs:
            sc = "".join(sorted(s))
            #if sc in dic:
            dic[sc].append(s)
            #else:
            #    dic[sc] = [s]
        
        #for k in dic:
        #    ans.append(dic[k])
        return dic.values()  # so we don't need ans

# solution 2: count character then categorize
# Time: O(NK)
# Space:O(K), 26K for ans dict
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()