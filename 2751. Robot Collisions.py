# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Approach:
# 1. We will first sort the robots based on their positions.
# 2. We will then iterate through the robots and check if the robot is moving in the same direction as the previous robot.
# 3. If the robot is moving in the same direction, we will add it to the stack.
# 4. If the robot is moving in the opposite direction, we will check if we can eliminate the robot or not.
# 5. If the robot can be eliminated, we will eliminate it and update the health of the robot.
# 6. If the robot can't be eliminated, we will add it to the stack.
# 7. Finally, we will return the health of the robots in the order they were given.

# Notes: I missed the adding back part and skipping initial robots moving to the left.

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [[positions[ind], healths[ind], directions[ind], ind] for ind in range(n)]
        robots.sort()
        stack = []

        for robot in robots:
            if robot[2] == "R" or not stack or stack[-1][2] == "L":
                stack.append(robot)
                continue

            if robot[2] == "L":
                add = True
                while stack and stack[-1][2] == "R" and add:
                    last_health = stack[-1][1]
                    if robot[1] > last_health:
                        stack.pop()
                        robot[1] -= 1
                    elif robot[1] < last_health:
                        stack[-1][1] -= 1
                        add = False
                    else:
                        stack.pop()
                        add = False
                if add:
                    stack.append(robot)
        return [robot[1] for robot in sorted(stack, key=lambda robot: robot[3])]