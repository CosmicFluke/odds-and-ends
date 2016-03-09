### Asher Minden-Webb's odds-and-ends Library

This repository is a collection of assorted personal projects by Asher Minden-Webb.  Currently consists of the following files & packages:

####`avltree`
Python implementations of:
* Binary Search Tree, in module `bstbase`, using a node class with functions for search and insert.
 * No container class included.
 * Deletion not yet implemented
* AVL Tree, in module `avltree` extending the BST node class and new implementations for search and insert.
 * No container class included
 * Deletion not yet implemented
* Ordered Weighted Set, in module `orderedweightedset`, an abstract data type using AVL trees and heap operations.
 * Implemented using a container class, `OrderedWeightedSet`
 * See documentation in `orderedweightedset.py` for more information

####`gameoflife-react`
Simple web app using React.js to build a Game of Life simulation
* Includes python HTTP server script (using std library http.server) to run app from http://localhost:8000
* This was my first time writing an app in JavaScript or React

####`matrixmult`
* Python script that parses a text file containing a sequence of matrices, calculates the matrix product, and prints the formatted product to stdout

####`projecteuler`
* Collection of solutions to Project Euler problems
 * Python: problems 8-20 (except 10 and 19)
 * Java: problem 4
 
####`bt_iterators`
Iterators for binary trees
* Two iterators: one for DFS traversal (stack) and one for BFS traversal (queue)
* Contains an iterable BTNode class which returns a stack iterator

####`maze_pathfinder`
Implementation of a solution to an interview problem I was given.
Given a 2-D array representing a maze, where
 * Value of 0 represents walls
 * Value of 1 represents paths
 * Value of 9 represents goal
is_path(maze) returns true if there is a path from (0, 0) to the goal cell.
