###
# one pass solution
# space complpexity O(n)
# time complexity O(n) <- not sure about searching in dict
###
class Solution:   # , , 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for idx, n in enumerate(nums):
            complement = target - n
            if complement in temp:
                return [temp[complement], idx]
            temp[n] = idx