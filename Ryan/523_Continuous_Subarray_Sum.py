# solution 1 - brute force
# Time: O(n^3), not O(n^2) since we have to so sum, which cost O(n)
# Space: O(1)

# solution 2 - dict
# Time: O(n)
# Space: O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = dict()
        total = 0
        dic[0] = -1
        for idx, num in enumerate(nums):
            total+=num
            remainder = total % k
            if remainder in dic:
                if idx - dic[remainder] >1:
                    return True
                else:
                    continue
            dic[remainder] = idx
        return False
        
        