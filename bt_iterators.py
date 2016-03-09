# Author: Asher Minden-Webb
# Date: March 1, 2016

# Binary Tree node, iterators, and non-recursive function examples

import functools

class BTNode:
    """ An iterable Binary Tree node """
    BFS = "bfs"
    DFS = "dfs"
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.mode = BTNode.DFS
    
    def __iter__(self):
        return BTStackIterator(self) if mdde == DFS else BTQueueIterator(self)
        
    def set_iterator(self, mode):
        """ Set the iterator mode to either BTNode.BFS or BTNode.DFS """
        if mode not in [BTNode.BFS, BTNode.DFS]:
            raise Exception("Invalid iteration mode")
        self.mode = mode

        
def tree_sum_stack(root):
    """ Return the sum of a binary tree's values """
    # Iterative algorithm utilizing a stack
    stack = [root]
    sum = 0
    while stack:
        node = stack.pop()
        if node:
            sum += node.value
            stack.append(node.left)
            stack.append(node.right)
    return sum


class BTIterator:
    """ Abstract class for a Binary Tree iterator """
    def __init__(self, root):
        """
        Initialize an iterator for the binary tree rooted at root 
        
        @param root: The root of the binary tree to iterate over
        @type root: BTNode
        """
        self._items = [root] if root else []
        
    def __iter__(self):
        return self

    def __next(self):
        raise NotImplementedError


class BTStackIterator(BTIterator):
    """ Binary tree iterator using DFS ordering """
    def __next__(self):
        """
        @param self: BTStackIterator
        @rtype: BTNode | None
        """
        if not self._items:
            raise StopIteration
        else:
            node = self._items.pop()
            if node.left:
                self._items.append(node.left)
            if node.right:
                self._items.append(node.right)
            return node


class BTQueueIterator(BTIterator): 
    """ Binary Tree iterator using BFS ordering """
    def __next__(self):
        """
        @param self: BTQueueIterator
        @rtype: BTNode | None
        """
        if not self._items:
            raise StopIteration
        else:
            node = self._items.pop(0)
            if node.left:
                self._items.append(node.left)
            if node.right:
                self._items.append(node.right)
            return node


def tree_sum_1(root):
    """ Return the sum of a binary tree's values """
    # Iterative algorithm using DFS iterator
    sum = 0
    for node in root:
        if node:
            sum += node.value
    return sum


def tree_sum_2(root):
    """ Return the sum of a binary tree's values """
    # Functional, non-recursive algorithm using reduce w/ DFS iterator
    return functools.reduce(
        lambda sum, node: sum if node is None else sum + node.value, root, 0)


def tree_height_2(root):
    """ Return the height of a binary tree """
    # Iterative algorithm using reverse DFS iterator and memoization
    heights = {None: 0}
    for node in list(root)[::-1]:
        heights[node] = 1 + max(heights[node.left], heights[node.right])
    return heights[root]