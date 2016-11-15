#!/usr/bin/env python3

# This module was an attempt to solve a problem presented at a Microsoft coding competition
# Test files test1.txt and test2.txt belong to Microsoft

# Work-in-progress -- not yet rigorously tested

__author__ = "Asher Minden-Webb"
__credits__ = ["Asher Minden-Webb", "Elias Tragas"]
__license__ = "GPL"
__version__ = "1.0.3"

__python_version__ = "3.x"
__dependencies__ = ["numpy"]

import numpy
import sys

FILENAME = "test2.txt"  # Default filename

def parse_file(filename):
    ''' (String) -> List of numpy.array
    Takes a text file of matrix input and parses into a list of matrices 
    (each an list of lists).  Text file must be formatted such that each row of 
    each matrix is bordered by "|" characters, every row of a matrix must be
    the same character width between "|" delimiters, and the first "|" of every
    row of a matrix must be at the same character position in each line.
    
    | matrix 1, row1 | | matrix 2, row 1 | | matrix 3, row 1 |
                       | matrix 2, row 2 | | matrix 3, row 2 |
                       | matrix 3, row 3 |
    
    Each numerical entry in each row is delimited by a space
    '''
    stream = open(filename)
    matrices = []
    row = 0
    num_matrices = 0
    
    # Get the number of matrices
    first_line = stream.readline()
    num_matrices = first_line.count("|") // 2
    
    # Get the character width of each matrix
    first_line_list = first_line.strip("|\n").split("| |")
    # each elements of matrix_widths corresponds to one matrix
    matrix_widths = [len(row) for row in first_line_list]
    
    # verify
    try:
        assert(len(matrix_widths) == num_matrices)
    except AssertionError:
        print("There appears to be a problem with the format of input text.")
        return None
    
    # initialize matrices; assume len(matrices) == len(matrix_widths)
    
    # matrix_width[i] is the character width between "|" delimiters in the 
    # input file for the matrix stored at matrices[i]
    matrices = [[[int(num.strip()) for num in matrix_first_row.strip().split()]] for matrix_first_row in first_line_list]
    
    # Parse the remaining lines
    for line in stream:
        # Iterate through matrices
        starting_index = 0
        for matrix_num in range(len(matrices)):
            # Get row width for this matrix
            row_width = matrix_widths[matrix_num]
            # Isolate the string containing this row, including "|" delimiters
            matrix_row = line[starting_index:starting_index + row_width + 2]
            # Trim this row from the current line (for next iteration)
            starting_index += row_width + 3
            # If this matrix has a row on this line of the input file...
            if "|" in matrix_row:
                # Parse the row and append it to matrices[matrix_num]
                matrix_row = matrix_row.strip("| ")
                matrices[matrix_num].append([int(num.strip()) for num in matrix_row.split()])
    
    stream.close()
    for matrix in range(len(matrices)):
        matrices[matrix] = numpy.array(matrices[matrix])
    return matrices

def multiply_matrices(matrix_list):
    ''' (List of numpy.array) -> numpy.array
    Returns the product of the matrices in matrix_list
    Precondition: matrix_list is a valid list of multiplicable numpy.array matrices
    '''
    # Start with first matrix as matrix product
    product = matrix_list[0]
    
    # Multiply each subsequent matrix by the matrix product
    for matrix in matrix_list[1:]:
        product = numpy.dot(product, matrix)
        
    return product

def matrix_to_string(matrix):
    ''' (numpy.array) -> String
    Builds a printable representation of the numpy.array matrix in the format:
    
    | r1c1 r1c2 r1c3 |
    | r2c1 r2c2 r2c3 |
    | r3c1 r3c2 r3c3 |
    '''
    matrix_string = ""
    matrix_list = matrix.tolist()
    concat_list = []
    for row in matrix_list:
        concat_list.extend(row)
    
    max_num = max(concat_list)
    min_num = min(concat_list)
    len_max = max(len(str(max_num)), len(str(min_num)))
    
    for row in matrix_list:
        row = [" " * (len_max - len(str(x))) + str(x) for x in row]
        matrix_string += "| " + " ".join(row) + " |\n"
        
    return matrix_string


# Script's main function
if __name__ == "__main__":
    
    # Get filename from arguments
    if len(sys.argv) == 1:
        file = FILENAME
    elif len(sys.argv) == 2:
        file = sys.argv[1]
    else:
        print("Usage: matrixmult.py [filename]")
        raise Exception("Invalid arguments")
        
    '''
    Sample input:
    |  8 20 15 | | -16 -15 -13   2  20 | | -19  11  -4 11 |
    | 19 -4  2 | |  15 -25 -12 -19 -20 | |  23  14 -13 15 |
                |  -6 -12  -8   6   5 | |   6  20 -22 16 |
                                        |   6  23 -22 18 |
                                        | -11 -10  21 19 |
    '''   
    
    # Parse the file
    multiplicands = parse_file(file)
    
    # # Print matrices
    # for matrix in npmatrices:
    #     for row in matrix:
    #         print(row)
    #     print()
    
    # Get product
    product = multiply_matrices(multiplicands)
    
    # Build output
    output = matrix_to_string(product)
    
    # Print output
    print(output)
        
