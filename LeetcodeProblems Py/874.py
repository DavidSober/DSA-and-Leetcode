class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        direction = ('north', 'east', 'south', 'west')
        curr_dir = 0
        coords = [0, 0]
        ans = float("-inf") # smallest dist
        h_obstacles = set()
        for obstacle in obstacles: # hash all obstacles 
            h_obstacles.add((obstacle[0], obstacle[1]))
        for command in commands:
            if 0 <= command <= 9:
                # movement 
                for i in range(command):
                    if curr_dir == 0: # north
                        coords[1] += 1
                        if (coords[0], coords[1]) in h_obstacles:
                            coords[1] -= 1
                    elif curr_dir == 1: # east
                        coords[0] += 1
                        if (coords[0], coords[1]) in h_obstacles:
                            coords[0] -= 1
                    elif curr_dir == 2: # south
                        coords[1] -= 1
                        if (coords[0], coords[1]) in h_obstacles:
                            coords[1] += 1
                    elif curr_dir == 3: # west
                        coords[0] -= 1
                        if (coords[0], coords[1]) in h_obstacles:
                            coords[0] += 1
                ans = max(ans, coords[0]**2 + coords[1]**2) 
            elif command == -1:
                # print("dir is", direction[curr_dir], curr_dir)
                curr_dir = (curr_dir + 1) % 4
                
                # print("dir is", direction[curr_dir], curr_dir)
            elif command == -2:
                curr_dir = (curr_dir - 1) % 4

        return ans