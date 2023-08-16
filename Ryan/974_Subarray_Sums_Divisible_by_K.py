# solution 0: brute force
# Time: O(n^2)
# Space: O(1)
# try all subarray

# solution 1: hashmap (difference between accumulation)
# Time: O(n)
# Space:O(min(n,k))
# if x%k==y%k, then (x-y)%k==0
# keep accumulating the sum and use hashmap to count the appear time of the remainder of accumulation   
# Once the same remainder appears again, we get subarrays base on the number of remainder, so add into ans variable
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        accumulation = 0
        dic = {0:1}
        ans = 0
        for val in nums:
            accumulation+=val
            valid = dic.get(accumulation%k, 0)
            ans+=valid
            dic[accumulation%k]=valid+1
        return ans