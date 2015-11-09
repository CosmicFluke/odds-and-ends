# AVL Tree Implementation

from bstbase import *

class AVLNode(BSTNode):
    ''' AVL Tree node '''
    
    def __init__(self, key, left=None, right=None):
        ''' Node Constructor '''
        super().__init__(key, left, right)
        self.height = 0
        

def calcAVLbf(root):
    ''' (BSTNode) -> int
    Calculate the Balance Factor of a BST tree rooted at BSTNode root
    '''
    if root is None or root.isLeaf():
        return 0
    return \
        (getBSTHeight(root.right) if root.hasRight() else 0) - \
        (getBSTHeight(root.left) if root.hasLeft() else 0)

    
def rotate_right(root):
    ''' (AVLNode) -> AVLNode
    Rotates a subtree right at root, and returns new root '''
    
    # Perform rotation
    new_root = root.left
    temp = new_root.right
    new_root.right = root
    root.left = temp
    
    # Update bookkeeping values (size, height, bf)
    UpdateAVLBooks(root, new_root, temp)
    
    return new_root
    
def rotate_left(root):
    ''' (AVLNode) -> AVLNode
    Rotates a subtree left at root, and returns a new root '''
    
    # Perform rotation
    new_root = root.right
    temp = new_root.left
    new_root.left = root
    root.right = temp
    
    # Update bookkeeping values (size, height, bf)
    UpdateAVLBooks(root, new_root, temp)
    
    return new_root
    
def UpdateAVLBooks(root, new_root, temp):
    # Old root
    left_height = root.left.height if root.hasLeft() else -1
    right_height = root.right.height if root.hasRight() else -1
    root.height = max(left_height, right_height) + 1
    temp_size = temp.size if temp is not None else 0
    root.size = root.size - new_root.size + temp_size
    root.bf = left_height - right_height
    
    # New root
    left_height = new_root.left.height if new_root.hasLeft() else -1
    right_height = new_root.right.height if new_root.hasRight() else -1
    new_root.height = max(left_height, right_height) + 1
    left_size = new_root.left.size if new_root.hasLeft() else 0
    right_size = new_root.right.size if new_root.hasRight() else 0
    new_root.size = left_size + right_size + 1
    new_root.bf = left_height - right_height


def AVLInsert(root: AVLNode, node: AVLNode):
    ''' (AVLNode, AVLNode) -> AVLNode
    Adds the AVLNode node to the AVLNode root.  Returns the new root.
    Also updates height and balance factors, and rebalances. '''
    
    if root is None:
        return node
    root.size += 1
    if node.key > root.key:
        if root.hasRight():
            root.right = AVLInsert(root.right, node)
        else:
            root.right = node
    elif node.key <= root.key:
        if root.hasLeft():
            root.left = AVLInsert(root.left, node)
        else:
            root.left = node
                
    left_height = root.left.height if root.hasLeft() else -1
    right_height = root.right.height if root.hasRight() else -1
    root.height = max(left_height, right_height) + 1
    if not root.isLeaf():
        root = rebalance(root)
    return root
    
def rebalance(root):
    
    root.bf = \
        (root.left.height if root.hasLeft() else -1) - \
        (root.right.height if root.hasRight() else -1)
    
    if root.bf > 1:
        # need to rotate right
        a = root
        b = root.left
        # Can assume root.left is not None because root.bf > 1
        if b.bf == -1:
            # New node is on the left child's right subtree
            # Need to rotate root's left subtree to the left first
            a.left = rotate_left(b)
        new_root = rotate_right(a)
        return new_root
        
    if root.bf < -1:
        # need to rotate left
        a = root
        b = root.right
        # Can assume root.right is not None because root.bf < -1
        if b.bf == 1:
            # New node is on right child's left subtree
            # Need to rotate root's right subtree to the right first
            a.right = rotate_right(b)
        new_root = rotate_left(a)
        return new_root
        
    return root