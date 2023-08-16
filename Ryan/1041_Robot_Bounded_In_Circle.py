# Solution 1
# Time: O(N)
# Space: O(1)
# Runtime: 20 ms, faster than 99.27% of Python3 online submissions for Robot Bounded In Circle.
# Memory Usage: 14 MB, less than 91.75% of Python3 online submissions for Robot Bounded In Circle.

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x_position = 0
        y_position = 0
        direction = [[0,1],(1,0),(0,-1),(-1,0)]
        dir_type = 0
        for ins in instructions:
            if ins == "L":
                dir_type = (dir_type-1)%4
            elif ins == "R":
                dir_type = (dir_type+1)%4  
            elif ins == "G":
                x_position += direction[dir_type][0]
                y_position += direction[dir_type][1]
                
        if dir_type!=0 or (x_position==y_position==0):
            return True
        else:
            return False

# There are two cases of limit cycle trajectory.
# 1. after one cycle, robot returns to original coordinate and faces North.
# 2. after each cycle, robot faces different direction.

# Prove of 2:
# In the beginning, the robot faces North, so it's easy to infer that the robot must face North again after 4 rounds.
# And we want to prove that the robot will return to original position after 4 rounds:
#   Suppose after first round, the robot position is:
#     x2 = x1 + Δx
#     y2 = y1 + Δy
#   Then: 
#     case 2-1 : robot face East after first round:
#       x4 = x1 + Δx + Δy - Δx - Δy = x1
#       y4 = y1 + Δy - Δx - Δy + Δx = y1
#     case 2-2: ...