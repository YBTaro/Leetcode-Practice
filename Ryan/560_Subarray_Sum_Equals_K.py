# solution 1 - brute force
# Time: O(n^3)
# Space: O(1)

# solution 2 - accumulation - Time Limit Exceeded
# Time: O(n^2)
# Space: O(n)
class Solution:
	def subarraySum(self, nums:List[int], k:int) -> int:
		accumulation = [0]
		for num in nums:
			accumulation.append(accumulation[-1]+num)

		ans = 0
		for i in range(len(accumulation)):
			for j in range(i+1, len(accumulation)):
				if accumulation[j] - accumulation[i] == k:
					ans+=1
		return ans


# solution 2 - accumulation2 - Time Limit Exceeded
# Time: O(n^2)
# Space: O(1)
class Solution:
    def subarraySum(self, nums:List[int], k:int) -> int:
        ans = 0
        for i in range(len(nums)):
            accu = 0
            for j in range(i, len(nums)):
                accu += nums[j]
                if accu == k:
                    ans+=1
        return ans

# solution 3 - hashmap
# Time: O(n)
# Space:O(n)

# this algorithm is like # solution 2 - accumulation1,
# when it comes to a new number, we can get a new accumulate, 
# from the beginning of array to this number, and we will check if 
# new accu - k exist in hashmap of not, if yes, it means sun[i]-sum[j]==k, 
# means sum of j to i is k, so we add the ans by the count of dic[j] 

class Solution:
    def subarraySum(self, nums:List[int], k:int) -> int:
        ans = 0
        dic = collections.defaultdict(lambda:0)
        dic[0] = 1
        accu = 0
        for i in range(len(nums)):
            accu += nums[i]
            if accu-k in dic:
                ans += dic[accu-k]
            dic[accu]+=1
        return ans
            