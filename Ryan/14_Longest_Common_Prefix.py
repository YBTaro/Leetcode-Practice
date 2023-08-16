# prefix tree
# by dict, seems not good enough
class Solution:
    
    def rec_build(self, root, s):
        if len(s)==0:
            return ""
        c = s[0]
        if c not in root:
            print("?")
            root[c]=dict()
            return self.rec_build(root[c], s[1:])
        else:
            return c + self.rec_build(root[c],s[1:])
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptree = dict()
        ans = strs[0]
        self.rec_build(ptree, strs[0])
                    
        for s in strs:
            prefix = self.rec_build(ptree, s)
            print(prefix)
            if len(prefix) < len(ans):
                ans = prefix
        return ans
        
    