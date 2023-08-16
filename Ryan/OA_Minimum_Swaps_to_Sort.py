# Minimum Swaps to Sort 
# OA question, the key is about to find the number of node in each cycle
# https://practice.geeksforgeeks.org/problems/minimum-swaps/1
# Time:O(nlogn)
# Space:O(n)
class Solution:
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#Code here
		
		sort_arr = [(idx, num) for idx, num in enumerate(nums)]
		sort_arr.sort(key = lambda x: x[1])
		
		swap = 0
		visited = [0] * len(nums)
		for to_idx, (start_idx, num) in enumerate(sort_arr):
		    if to_idx!=start_idx and not visited[start_idx]:
    		    while not visited[start_idx]:
    		        visited[start_idx] = 1
    		        swap +=1
    		        to_idx = start_idx
    		        start_idx = sort_arr[start_idx][0]
    		    swap-=1
		return swap