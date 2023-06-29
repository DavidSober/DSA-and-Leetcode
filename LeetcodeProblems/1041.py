# here is my solution to the robot bounded in circle problem
# this took about 40 mins to make and 20 mins to debugg (figuring out criteria for
# knowing whether or not we are in a circle over time)
# beats 5% in time and 71% in space

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        orientation = [(0,1), (-1,0), (0,-1), (1,0) ] # North, West, South, East
        change_dir = {'L': 1, 'R':-1}
        curr_dir = 0
        curr_coords = [0,0]
        def valid_dir(curr_dir, new_dir): # takes in change in new dir and returns the index of orientation
            curr_dir += change_dir[new_dir]
            if curr_dir > 3:
                return 0
            elif curr_dir < 0:
                return 3
            else:
                return curr_dir
        max_dist = [0,0]
        D1 = None
        cycles = 10
        for i in range(cycles):
            for instruction in instructions:
                if instruction == 'L' or instruction == 'R':
                    curr_dir = valid_dir(curr_dir, instruction) # update curr direction
                elif instruction == 'G':
                    curr_coords[0] += orientation[curr_dir][0]
                    curr_coords[1] += orientation[curr_dir][1]  
                max_dist[0] = max(max_dist[0], abs(curr_coords[0]))
                max_dist[1] = max(max_dist[1], abs(curr_coords[1]))
                if i == cycles // 2:
                    D1 = max_dist.copy()
        if max_dist[0] > D1[0] or max_dist[1] > D1[1]:
            return False
        return True