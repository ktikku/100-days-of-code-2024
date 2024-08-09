from collections import defaultdict
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        expected_sum = 45
        count = 0
        print(len(grid), len(grid[0]))
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                print('starting index:', i, j)
                check = True
                elem_set = set()
                elem_set.add(grid[i][j])
                elem_set.add(grid[i][j + 1])
                elem_set.add(grid[i][j + 2])
                elem_set.add(grid[i + 1][j])
                elem_set.add(grid[i + 1][j + 1])
                elem_set.add(grid[i + 1][j + 2])
                elem_set.add(grid[i + 2][j])
                elem_set.add(grid[i + 2][j + 1])
                elem_set.add(grid[i + 2][j + 2])
                print(len(elem_set))
                if len(elem_set) != 9:
                    continue
                for element in elem_set:
                    if element > 9:
                        check = False
                        continue
                sum = (
                    grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
                    grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] +
                    grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                )
                
                row_one = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                row_two = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
                row_three = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                is_rows_sum_equal = row_one == row_two == row_three

                column_one = grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                column_two = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                column_three = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
                is_column_sum_equal = column_one == column_two == column_three

                diagonal_one = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                diagonal_two = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j]
                is_diagonal_sum_equal = diagonal_one == diagonal_two
                print(is_rows_sum_equal, is_column_sum_equal, is_diagonal_sum_equal, diagonal_one == row_one == column_one, diagonal_one, row_one, column_one)
                if sum == expected_sum and diagonal_one == row_one == column_one and is_diagonal_sum_equal and is_rows_sum_equal and is_column_sum_equal and check:
                    count += 1
        return count