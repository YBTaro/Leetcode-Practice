# solution 1 - brute force
# Time: O(n^2)
# Space: O(1)
# Just compare every pair

# solution 2 - greedy
# Time: O(nlogn)
# Space: O(n) for sort
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True