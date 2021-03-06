#!/usr/bin/env python3

__author__ = "Asher Minden-Webb"
__title__ = "Project Euler Problem 11: Largest product in a grid"
__date_created__ = "2014/09/24"

'''
URL: https://projecteuler.net/problem=11

In the 20×20 grid below (see GRID), four numbers along a diagonal line have 
been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?
'''

import time, random

GRID = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''

def build_grid(text: str) -> list:
    '''
    Builds a two-dimensional list from the given string.  Expected
    input has uniformly-long newline-delimited rows of two-digit numbers, 
    separated by spaces.  The input string has leading and trailing newline 
    characters.
    '''
    
	# Build list of lists, where each sub-list represents a row of integers
    return [[int(num) for num in line.strip().split()] for line in text.strip().split('\n')]

def row_product(grid: list) -> int:
	''' 
	Finds the greatest product of 4 horizontally adjacent numbers in the grid
	'''	
    greatest = 0
    for row in grid:
        i = 0
        while i < len(row) - 3:
            group, product = [row[i + x] for x in range(4)], 1
            for x in group:
                product *= x
            if product > greatest:
                greatest, winners = product, \
                    [[grid.index(row), i + x] for x in range(4)]
            i += 1
    return greatest, winners

def col_product(grid: list) -> int:
	''' 
	Finds the greatest product of 4 vertically adjacent numbers the grid 
	'''
    greatest = 0
    for col in range(len(grid[0])):
        row = 0
        while row < len(grid) - 3:
            group, product = [grid[row + x][col] for x in range(4)], 1
            for x in group:
                product *= x
            if product > greatest:
                greatest, winners = product, \
                    [[row + x, col] for x in range(4)]
            row += 1
    return greatest, winners

def diag_product(grid: list) -> int:
	'''
	Finds the greatest product of 4 diagonally adjacent numbers in the grid
	'''
    greatest = 0
    depth = len(grid) - 3
	# Check each row
    for row in range(depth):
        width = len(grid[row]) - 3
        col, i = 0, 0
		# Check diagonal top-left to bottom-right
        while col < width:
            group, product = [(row + x, col + x) for x in range(4)], 1
            for x in group:
                product *= grid[x[0]][x[1]]
            if product > greatest:
                greatest, winners = product, group
            col += 1
		# Check diagonal top-right to bottom-left
        while i < width:
            col = width + 2 - i
            group, product = [(row + x, col - x) for x in range(4)], 1
            for x in group:
                product *= grid[x[0]][x[1]]
            if product > greatest:
                greatest, winners = product, group
            i += 1
    return greatest, winners
		
def grid_to_str(grid: list) -> None:
	''' Creates a string representation of a list of lists of numbers '''
	# Get the number of digits in the largest number in the grid
	max_num = len(str(max([max(row) for row in grid])))
	
	# Define lambda function to convert a number to a digit string with leading zeros
	num_to_string = lambda num: '0' * (digits - len(str(num))) + str(num) + ' '
	
	# Build a list where each row is a list of converted digit strings
	rows_of_strings = [[num_to_string(num) for num in row] for row in grid]
	
	# Convert inner lists to strings, join those strings, and return final string
	return '\n'.join([''.join(row) for row in rows_of_strings])
	


# Lambda function that generates a random grid for testing
generate_random_grid = (lambda rows, cols:
	[[random.randint(1,99) for x in range(cols)] for row in range(rows)])
	
# Create a 4x4 test grid (Not currently utilized)
test_table_4x4 = generate_random_grid(4,4)


# ------- Get Results Using Given Grid -------- #

# Start a timer
start = time.time()

table = build_grid(GRID)  # Table is the default (given) grid

# Get the greatest product in each direction; map products to lists of indices
directions = {x[0]:x[1] for x in \
              (col_product(table), row_product(table), diag_product(table))}
			  
# Get max product
greatest, locations = max(directions), directions[max(directions)]

# Stop Timer
end = time.time()

print(grid_to_str(table))
print(greatest)
print("Elapsed:", end - start)

