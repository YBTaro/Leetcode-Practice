# solution 1 - greedy - if the interviewer doesn't allow to modify
# Time: O(n)
# Space:O(1)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        i = 0
        for interval in intervals:
            if interval[0] < newInterval[0]:
                ans.append(interval)
                i+=1
        
        if ans and ans[-1][1] >= newInterval[0]:
            ans[-1][1] = max(ans[-1][1], newInterval[1])
        else:
            ans.append(newInterval)
        
        for j in range(i,len(intervals)):
            if ans[-1][1] >= intervals[j][0] :
                ans[-1][1] = max(ans[-1][1], intervals[j][1])
            else:
                ans.extend(intervals[j:])
                break
        return ans

# solution 2 - binary search - if the interviewer allows us to modify the input
# Time: O(logn)
# Space:O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        ans = []
        def BinarySearch1(target):
            left, right = 0, len(intervals)-1
            while left<=right:
                m = (left+right)//2
                if intervals[m][1] >= target:  # the difference
                    right = m-1
                else:
                    left = m+1 
            return left
        
        def BinarySearch2(target):
            left, right = 0, len(intervals)-1
            while left<=right:
                m = (left+right)//2
                if intervals[m][0] > target: # the difference
                    right = m-1
                else:
                    left = m+1 
            return left

        start_overlap = BinarySearch1(newInterval[0])
        end_overlap = BinarySearch2(newInterval[1])

        if start_overlap < end_overlap:
            newInterval[0] = min(newInterval[0], intervals[start_overlap][0])
            newInterval[1] = max(newInterval[1], intervals[end_overlap-1][1])
            return intervals[:start_overlap] + [newInterval] + intervals[end_overlap:]
        if start_overlap == end_overlap:
            return intervals[:start_overlap] + [newInterval] + intervals[start_overlap:]
        return [[1,2]]

