# solution 1 - left and right list
# Time : O(N)
# Space: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]
        for i in range(len(nums)-1):
            left.append(left[-1]*nums[i])
            right.append(right[-1]*nums[len(nums)-1-i])
        
        return [left[i]*right[len(nums)-1-i] for i in range(len(nums))]

# solution 2 - two pointer
# Time: O(N)
# Space: O(1), O(N) for ans

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 1,1
        ans = [1]*(len(nums))
        for lp in range(len(nums)-1):
            rp = len(nums)-1-lp
            left*=nums[lp]
            right*=nums[rp]
            ans[lp+1]*=left
            ans[rp-1]*=right
        return ans