# Solution 1, sort and scan by two pointer
# For the main funcion
# 1. sort the input array
# 2. iterate through the input array:
#    a. if the current value is greater than 0, break the loop because the rest value are all positive
#	 b. if the value equals to the previous value, skip it
#    c. do twoSum for the current position i
#
# For the twoSum function
# 1. set two pointer "left" to i+1, "right" to the end of the input array
# 2. while left pointer on the left of right pointer:
#    a. if sum of left and right is greater than target, decrease right pinter
#    b. if sum of left and right is less that target, increase left pointer
#    c. if sum of left and right equals to target, save the pair. Then increase left and decrease right to different values to avoid duplicates

# time: O(n^2)  (O(n) for twoSum and we call it for n times)
# space: O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for idx, pivot in enumerate(nums):
            if pivot > 0:
            	break
            if idx>0 and pivot == nums[idx-1]:
                continue
            pairs =self.twoSum(idx, nums)
            for p in pairs:
                p.append(pivot)
                ans.append(p)
        return ans
            
    def twoSum(self, idx, nums):
        pairs = []
        target = 0-nums[idx]
        left = idx+1
        right = len(nums)-1
        while left<right:
            while left<right and nums[left]+nums[right]>target:
                right-=1
            while left<right and nums[left]+nums[right]<target:
                left+=1
            if left<right and nums[left]+nums[right]==target:
                if len(pairs)==0 or pairs[-1][0]!=nums[left]:
                    pairs.append([nums[left],nums[right]])
                right-=1
                left+=1
        return pairs
##########################################
# Solution 2, un-sort and use hash
# For the main function threeSum
# 1. iterate the pointer i through the input array:
#    A. if the current value has seen before, skip it
#    B. iterate the pointer j through the input array from the position i+1
#       a. find complement = -i -j
#       b. if the complement is in "seen set", save (i,j,complement) in answer
#       c. if not, save j in "seen set"
# time: O(n^2), but since we use hash set, it will cost more time to compare the values
# space: O(n) for hash set

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans, dup_i = set(),set()
        for idx, i in enumerate(nums):
            if i not in dup_i:
                dup_i.add(i)
                seen = set()
                for j in nums[idx+1:]:
                    complement = - i - j
                    if complement in seen:
                        ans.add(tuple(sorted([i,j,complement])))
                    else:
                        seen.add(j)
        return ans 
##########################################
# solution 3, sort and use one-pass hash
# For the main function threeSum:
# 1. sort the input array
# 2. iterate through the input array:
#    a. if the current value greater that 0, than break
#    b. if the current value NOT equals to the previous value, do function twoSum for the current position i
#
# For the function twoSum
# 1. start from the position j = i+1
# 2. while j is not the end of the input array
#    a. find complement = -i -j
#    b. if the complement is in the seen set, save i,j,complement into answer array, then increase j until a new value to avoid duplicate value
#    c. add j into seen set 
#
# time: O(n^2)
# space: O(n) for hashset

class Solution:
	def threeSum(self, nums:List[int]) -> List[List[int]]:
		ans = []
		nums.sort()
		for idx in range(len(nums)):
			if nums[idx]>0:
				break
			if idx==0 or nums[idx]!=nums[idx-1]:
				self.twoSum(nums, idx, ans)
		return ans
	def twoSum(self, nums, i_idx, ans):
		seen = set()
		j_idx=i_idx+1
		while j_idx<len(nums):
			complement = -nums[i_idx] -nums[j_idx]
			if complement in seen:
				ans.append([nums[i_idx], nums[j_idx], complement])
				while j_idx+1 < len(nums) and nums[j_idx]==nums[j_idx+1]:
					j_idx+=1
			seen.add(nums[j_idx])
			j_idx+=1



###########################

class Solution:
    def threeSum(self, nums:List[int]) -> List[List[int]]:
        # sort nums
        # iterate through the array, for each elememt
        # if the current value larger than 0, it's impossible to get 0, break
        # if the current value same as the previous one, continue
        # else: do two sum to get the complement of the current value
        # combine the current value with the pairs returned by two_sum
        nums.sort()
        ans = []
        for idx, num in enumerate(nums):
            if num>0:
                break
            if idx>0 and nums[idx]==nums[idx-1]:
                continue
            complement = 0 - num
            pairs = self.twoSum(nums[idx+1:], complement)
            for (a,b) in pairs:
                ans.append([num,a,b])
        return ans

    def twoSum(self, nums, target):
        pairs = []
        l,r = 0, len(nums)-1
        while l<r:
            s = nums[l]+nums[r]
            if s<target:
                l+=1
            elif s>target:
                r-=1
            else:
                pairs.append((nums[l],nums[r]))
                l+=1
                r-=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
                while l<r and nums[r]==nums[r+1]:
                    r-=1
        return pairs

