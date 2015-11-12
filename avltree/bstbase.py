#!/usr/bin/env python3

# BST Node Class and Operations
# The BST is not implemented with a container class here

__author__ = "Asher Minden-Webb"
__credits__ = ["Asher Minden-Webb", "Elias Tragas"]
__license__ = "GPL"
__version__ = "1.0.3"

__python_version__ = "3.x"

import math

class BSTNode:
    ''' AVL Tree node '''
    
    def __init__(self, key, left=None, right=None):
        ''' Node Constructor '''
        self.key = key
        self.size = 1       # Number of nodes in subtree rooted at self
        self.left = left    # Left child
        self.right = right  # Right child
        self.height = 0
        self.bf = 0
        
    def isLeaf(self):
        return not self.hasLeft() and not self.hasRight()
        
    def hasLeft(self):
        return self.left is not None
        
    def hasRight(self):
        return self.right is not None
        
    def updateSize(self):
        self.size = \
        (self.left.size if self.hasLeft() else 0) + \
        (self.right.size if self.hasRight() else 0) + 1
        
    def __str__(self):
        return str(self.key)

def BSTRank(root, node):
    ''' Precondition: node is in the AVL tree rooted at root '''
    if node == root:
        if node.hasLeft():
            return node.left.size
        return 1
    if node.key > root.key:
        return root.size + AVLRank(root.right, node)


def make_BST_BFS_queue(root):
    queue = []
    temp_queue = [root, '\n']
    while len(temp_queue) > 0 and len(temp_queue) != (temp_queue.count('\n') + temp_queue.count(None)):
        hold = temp_queue.pop(0)
        if hold == '\n':
            queue.append(hold)
            temp_queue.append('\n')
            continue
        if hold is not None:
            temp_queue.append(hold.left)
            temp_queue.append(hold.right)
        else: temp_queue.extend([None, None])
        queue.append(hold)
    return queue
    
def print_BST(root):
    queue = make_BST_BFS_queue(root)
    height = math.floor(math.log2(len(queue) - queue.count(None) - queue.count("\n")))
    bottom_row = (2 ** height) / 2
    row = 0
    for i in queue:
        print(' ' * ((5 - len(str(i))) * (height - row + 2)), end='')
        if i == "\n":
            row += 1
        print(i, end='')
    
def getBSTHeight(root):
    ''' (BSTNode) -> int 
    '''
    if root is None:
        return -1
    if root.isLeaf():
        return 0
    return 1 + max(getBSTHeight(root.left), getBSTHeight(root.right))
        
def BSTInsert(root: BSTNode, node: BSTNode):
    ''' (BSTNode, BSTNode) -> BSTNode
    Adds the BSTNode node to the BSTNode root.  Returns the new root.
    Also updates height and balance factors. '''
    
    if root is None:
        return node
    root.size += 1
    if node.key > root.key:
        if root.hasRight():
            BSTInsert(root.right, node)
            root.bf = (root.left.height if root.hasLeft() else -1) - root.right.height
        else:
            root.right = node
            if not root.hasLeft():
                root.height += 1
                root.bf -= 1
    if node.key <= root.key:
        if root.hasLeft():
            BSTInsert(root.left, node)
            root.bf = root.left.height - (root.right.height if root.hasRight() else -1)
        else:
            root.left = node
            if not root.hasRight():
                root.height += 1
                root.bf += 1
    
    return root
    
def BSTSearch(root, key):
    ''' (BSTNode) -> BSTNode
    Returns the BSTNode with the given key in the BST rooted at BSTNode root.
    If key is not found, returns None
    '''
    
    if root is None:
        return None
    if root.key == key:
        return root
    if key > root.key:
        return BSTSearch(root.right, key)
    if key <= root.key:
        return BSTSearch(root.left, key)
        
        
    