# solution 1 - priotrity queue
# Time: O(nlogn)  (nlogn for sort, and so does heap build up by top-down way)
# Space: O(n), for heap and sort
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        min_heap = []
        intervals.sort(key = lambda x: x[0])
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= min_heap[0]:
                heapq.heappushpop(min_heap, intervals[i][1])
            else:
                heapq.heappush(min_heap, intervals[i][1])
        return len(min_heap)

# solution 2 - sort and greedy
# Time: O(nlog(n))
# Space: O(n) for time array and sort
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    	time = []
    	for start, end in intervals:
    		time.append([start,1])
    		time.append([end,-1])
    	time.sort()

    	room, max_room = 0, 0
    	for _, r in time:
    		room += r
    		max_room = max(max_room, room)
    		#assert room >=0
    	return max_room
