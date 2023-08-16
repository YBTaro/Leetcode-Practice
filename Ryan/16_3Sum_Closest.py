# Solution 1 - two pointer
# Time: O(N^2)
# Space: from O(logN) to O(n) for build-in sort, if we use select sort, we can get N(1)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = 10**6
        for idx in range(len(nums)-2):
            if idx==0 or nums[idx]!=nums[idx-1]:
                left = idx+1
                right = len(nums)-1
                while left < right:
                    total = nums[idx]+nums[left]+nums[right]
                    if abs(closest-target) > abs(total-target):
                        closest = total
                    if total > target:
                        right-=1
                    elif total < target:
                        left+=1
                    else:
                        return target
        return closest

# Solution 2 - binary search
# Time: O((N^2)* logN)
# Space:  from O(logN) to O(n) for build-in sort, if we use select sort, we can get N(1)

# fix two number -> O(N^2)
# bunary search -> O(logN)