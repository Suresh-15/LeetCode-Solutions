class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        dx, dy = 0, 1

        max_dist = 0
        obstacle_set = set(map(tuple, obstacles))

        for command in commands:
            if command == -2:  # turn left 90 deg
                dx, dy = -dy, dx
            elif command == -1:  # turn right 90 deg
                dx, dy = dy, -dx
            else:
                move = 0
                while move < command and (x + dx, y + dy) not in obstacle_set:
                    x += dx
                    y += dy
                    move += 1
                max_dist = max(x**2 + y**2, max_dist)

        return max_dist
