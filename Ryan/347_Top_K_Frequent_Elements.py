# Solution 1 - hash then heap
# Time: O(nlogk)
# Space: O(n+k), O(n) for hash map, O(k) for heap
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)
        # Time of heap:
        # first k elements: O(klogk)
        # them, n-k elements: O((n-k)logk)
        # -> O(nlogk)
        # Time of heap to array (keep pop): O(klogk)
        
        
# https://docs.python.org/3/library/heapq.html
# heapq.nlargest(n, iterable, key=None)
  # Return a list with the n largest elements from the dataset defined by iterable. key, if provided, specifies a 
  # function of one argument that is used to extract a comparison key from each element in iterable 
  # (for example, key=str.lower). Equivalent to: sorted(iterable, key=key, reverse=True)[:n].


# solution 2 - quick select
# Time: O(N) in average case, O(N^2) for worst case
# Space: O(N) for hash map

# To analysis the time complexity, we can use Master Theorem:
# T(N) = T(N/2) + N = T(N/4) + N/2 + N = N + N/2 + N/4 + N/8 + .... = a0*(1-r^n)/(1-r) = 2N = O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        
        counter = collections.Counter(nums)
        keys = list(counter.keys())
        
        def quickselect(pivot_ori_idx, counter, keys, left, right) -> int :
            keys[pivot_ori_idx], keys[right] = keys[right], keys[pivot_ori_idx]
            pivot_key = keys[right]
            i = left
            for j in range(left, right):
                j_key = keys[j]
                if counter[j_key] < counter[pivot_key]:
                    keys[i], keys[j] = keys[j], keys[i]
                    i+=1
            keys[right], keys[i] = keys[i], keys[right]
            return i # correct pivot idx
        
        left = 0
        right = len(keys)-1
        while left <= right:
            pivot_idx = quickselect(random.randint(left, right), counter, keys , left, right)
            if pivot_idx==len(keys)-k:
                return keys[pivot_idx:]
            elif pivot_idx < len(keys)-k:
                left = pivot_idx+1
            else:
                right = pivot_idx-1
        