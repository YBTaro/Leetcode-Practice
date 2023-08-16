# Solution 1
# Time: O(NlogN) + O(MlogM)
# Space: O(1), ignore horizontalCuts and verticalCuts cut

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        horizontalCuts.insert(0,0)
        verticalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        #horizontalCuts = [0]+horizontalCuts+[h]
        #verticalCuts = [0]+verticalCuts+[w]

        Horizontal_Max = max([horizontalCuts[i+1] - horizontalCuts[i] for i in range(len(horizontalCuts)-1)])
        Vertical_Max = max([verticalCuts[i+1]-verticalCuts[i] for i in range(len(verticalCuts)-1)])

        return (Horizontal_Max*Vertical_Max) % (10**9+7)
        