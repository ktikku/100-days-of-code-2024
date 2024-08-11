class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        directions = [[0,1], [0, -1], [1, 0], [-1,0]]
        i = 0
        j = 0
        for command in commands:
            if command == "RIGHT":
                i = i + directions[0][0]
                j =  j +  directions[0][1]
            elif command == 'LEFT':
                i = i + directions[1][0]
                j = j +  directions[1][1]
            elif command == 'DOWN':
                i = i + directions[2][0]
                j = j +  directions[2][1]
            elif command == 'UP':
                i = i + directions[3][0]
                j = j +  directions[3][1]
        return (i * n) + j