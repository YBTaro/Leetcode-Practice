# Solution 0: brute forse
# for each element, find the max() of its right and left to compute the water on it.
# time : O(n^2)
# space: O(n)

# Solution 1:dynamic programming
# Let's improve solution 0, we use two array to store:
#  1. the greatest number on each element's left
#  2. the greatest number on each element's right
# By doing so, we only have to check these tow array to get the water on each element
# time: O(n)
# space: O(n+n)=O(n)

# Solution 2: stack
# keep big element in stack and pop small element to compute the water on it
# Time:O(n)
# space:O(n), but less than solution 1


# Solution 3: myself - two-point - minus version
# Time : O(n)
# Space: O(1)
#Runtime: 48 ms, faster than 92.48% of Python3 online submissions for Trapping Rain Water.
#   Memory Usage: 14.8 MB, less than 85.32% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        
        left = 0
        right = len(height)-1
        new = 0
        water_vol = 0
        water_level = 0
        
        while left!=right:
            if height[left]==0:
                left+=1
                new = left
                continue
            elif height[right]==0:
                right-=1
                new = right
                continue
            
            if water_level > 0:
                water_vol -= min(height[new], water_level)
                
            if min(height[left], height[right]) > water_level:
                ori_water_level = water_level
                water_level = min(height[left],height[right])
                water_vol += (water_level-ori_water_level) * (right - left -1)
            
            if height[left] < height[right]:
                left+=1
                new = left
            else:
                right-=1
                new = right
        return water_vol

# Solution 3: official solution - two-point - plus version
# Time : O(n)
# Space: O(1)
# Runtime: 40 ms, faster than 99.42% of Python3 online submissions for Trapping Rain Water.
# Memory Usage: 14.7 MB, less than 85.32% of Python3 online submissions for Trapping Rain Water.
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        water_vol = 0
        left = 0
        right = len(height)-1

        left_maxh = 0
        right_maxh = 0

        while left!=right:
            if height[left] < height[right]:
                if height[left] > left_maxh:
                    left_maxh = height[left]
                else:
                    water_vol += left_maxh - height[left]
                left+=1
            else:
                if height[right] > right_maxh:
                    right_maxh = height[right]
                else:
                    water_vol += right_maxh - height[right]
                right-=1
            pass
        return water_vol
            
        
            
        