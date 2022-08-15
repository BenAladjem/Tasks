import unittest

"""
    grid = [
        [1, 1, 2, 2, 2, 1, 1, 1],
        [1, 1, 2, 2, 2, 1, 0, 0],
        [0, 1, 1, 2, 2, 1, 1, 0],
        [0, 1, 1, 0, 2, 1, 0, 0],
        [0, 3, 3, 0, 0, 1, 2, 2],
        [0, 3, 0, 0, 3, 2, 2, 0],
        [0, 3, 3, 3, 3, 0, 0, 0],
    ]

This grid of integers represents countries. Each countries land is a contiguous
block of the same integer. The size of a country is the number of grid cells
contained within its border. 

Notes: 

Non-connected blocks of colour are separate countries
Diagonally adjacent blocks are not connected
"""
#
grid = [
        [1, 1, 1, 1],
        [1, 2 ,2, 2],
        [1, 1, 1, 1],
        [0, 0, 0, 0]]


def all_countries(grid):
    def explore_area(row, col, matrix, n, visited):
        sell = []
        sell.append(row)
        sell.append(col)
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
            return 0
        if matrix[row][col] != n:
            return 0
        if sell in visited:
            return 0
        visited.append(sell)
        result = 1
        result += explore_area(row - 1, col, matrix, n, visited)
        result += explore_area(row + 1, col, matrix, n, visited)
        result += explore_area(row, col - 1, matrix, n, visited)
        result += explore_area(row, col + 1, matrix, n, visited)
        return result

    visited = []
    count = []
    big_num = 0
    big_country_name = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) in visited:
                continue
            num = explore_area(r, c, grid, grid[r][c], visited)
            if num > 0:
                count.append(num)
            if big_num < num:
                big_num = num
                big_country_name = grid[r][c]
    count.append(big_country_name)
    return count


def count_countries(grid):
    list_countries = all_countries(grid)
    return len(list_countries) - 1


def largest_country(grid):
    list_countries = all_countries(grid)
    return list_countries[-1]


print(largest_country(grid))
print(count_countries(grid))


class TestCountries(unittest.TestCase):
    def test_count_countries_with_one_country(self):
        self.assertEqual(count_countries([[0]]), 1)

    def test_count_countries_with_two_countries(self):
        self.assertEqual(
            count_countries(
                [[0, 0],
                 [1, 1]]
            ),
            2
        )

    def test_count_countries_diagonally_unconnected(self):
        self.assertEqual(
            count_countries(
                [[1, 0],
                 [0, 1]],
            ),
            4
        )

    def test_largest_country(self):
        self.assertEqual(
            largest_country(
                [[1, 1, 1, 1],
                 [1, 2 ,2, 2],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0]]
            ),
            1
        )

if __name__ == '__main__':
    unittest.main()
