# Solution 1 - Two Pointer Approach
# Time:O(n)     *brute force: O(n^2)
# Space:O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height)-1
        while left != right:
            curr_area = min(height[right], height[left])*(right-left)
            max_area = max(max_area, curr_area)
            if(height[right] > height[left]):
                left+=1
            else:
                right-=1
        return max_area
            
#
#Proof:
#	Suppose the returned result is not the optimal answer. Then there must be a optimal answer, let's say the optimal container is from 
#   opt_left to opt_right, which can create the largest container, and we never visited these two points in the same time. Since our 
#   algorithm stops only when the two pointers meet, we must have visited one of them but not the other. WLOG(Without loss of generality), 
#   let's say we visit opt_left but not opt_right. In other words, the pointer stop at opt_left until:
#
#	1. The other pointer reach opt_left:
#		In this case, the iteration end. But the other pointer must have visited opt_right on its way from right end to a_ol. Contradiction to 
#       our assumption that we didn't visit a_or. 
#	2. The other pointer arrives at a value, say new_right, whose height is greater than opt_left before it arrives opt_right:
#		In this case, we do move opt_left, but that means the container of (opt_left to new_night) is greater than (opt_left to opt_right), which will cause Contradiction. 