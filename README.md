### Asher Minden-Webb's odds-and-ends Library

This repository is a collection of assorted personal projects by Asher Minden-Webb.  Currently consists of the following packages:

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

####`matrixmult`
* Python script that parses a text file containing a sequence of matrices, calculates the matrix product, and prints the formatted product to stdout

####`projecteuler`
* Collection of python solutions to Project Euler problems