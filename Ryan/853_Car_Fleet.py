# solution 1 - greedy
# Time: O(nlogn)
# Space: O(n)
class Solution:
    def catchup(self, target, a, b):
        dis_a = target - a[0]
        dis_b = target - b[0]
        time_a = dis_a / a[1]
        time_b = dis_b / b[1]
        if time_a >= time_b:
            return True
        return False
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sheet = len(position)
        slow_one = 0
        temp = sorted(zip(position, speed), key = lambda x: -x[0])
        for i in range(0,len(temp)-1):
            if self.catchup(target, temp[slow_one], temp[i+1]):
                sheet-=1
            else:
                slow_one = i+1
        return sheet