# solution 1 - dic and compare adjacent words
# Time: O(WL), where W = number of words, L = longest length of word
# SpaceL O(1) for dict
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = dict()
        for i in range(len(order)): # O(1)
            dic[order[i]]=i
        
        for i in range(len(words)-1):   # O(W)
            s1 = words[i]   # compare i and i+1
            s2 = words[i+1]
            for j in range(len(s2)): # O(L)
                if j > len(s1)-1:
                    break
                if dic[s1[j]]<dic[s2[j]]:
                    break 
                elif dic[s1[j]]>dic[s2[j]]:
                    return False
                elif j==len(s2)-1 and j < len(s1)-1:
                    return False
        return True

# official version, which is much simplier
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = dict()
        for i in range(len(order)):
            dic[order[i]]=i
        
        for i in range(len(words)-1):  # compare i and i+1
            s1 = words[i]
            s2 = words[i+1]
            for j in range(len(s1)):
                if j > len(s2)-1:
                    return False
                if dic[s1[j]]!=dic[s2[j]]:
                    if dic[s1[j]] > dic[s2[j]]:
                    	return False
                    break
        return True