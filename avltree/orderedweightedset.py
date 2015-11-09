# Implementation of an Ordered Set with Weighted Keys
# Based on CSC263 midterm question
# Implemented using AVL Tree and Heap

from avltree import *

class CountingAVLNode(AVLNode):
    '''
    Augmented AVL Tree node
    Supports INC-COUNT(key) and DEC-BIG-COUNT() operations
    '''
    
    def __init__(self, key, data=None):
        ''' Must provide integer key.  May also provide any object as "data",
        and an initial count/weight. '''
        super().__init__(key, left, right)
        
        self.data = data    # Any data associated with this node's key
        self.count = 0      # The count (weight) associated with this node's key
        self.heap = None    # Associated heap (priority queue for count values)
        
        # Initialize value, used for AugHeapIncreasePriority
        self.heapIndex = -1
        
        # If a specific heap and count was provided at instantiation, 
        # insert node into heap
        if self.count > 0:
            AugHeapInsert(self.heap, self)
            
        
    def __repr__(self):
        return str((self.__str__(), str(self.count)))
        
        
class OrderedWeightedSet:
    ''' Consists of an ordered set of keys V, where each key has an associated 
    non-negative count, or 'weight'.  Initially, the count for every key is 0. 
    Supports two operations in addition to add():
    INC_COUNT(v)
    DEC_BIG_COUNT()
    '''
    
    def __init__(self):
        ''' (OrderedWeightedSet) -> None
        Constructor for OrderedWeightedSet '''
        self.root = None
    
    def add(self, key):
        ''' (OrderedWeightedSet, int) -> None
        Adds a key to the OrderedWeightedSet key set.  All keys begin with count==0 '''
        
        new_node = CountingAVLNode(key)
        if self.root is None:
            self.root = new_node
            self.root.heap = []
        else:
            # Ensure new node gets pointer to the shared heap
            new_node.heap = self.root.heap
            # Insert into AVL tree
            self.root = AVLInsert(self.root, new_node)
    
    def INC_COUNT(self, v):
        ''' (OrderedWeightedSet, int) -> None
        Increments the count associated with the key v '''
        
        # Find the node for key v
        x = BSTSearch(self.root, v)                             # O(log n)
        # If its count is zero, increment and add to heap
        if x.count == 0:
            x.count = 1
            AugHeapInsert(x.heap, x)                            # O(log n)
        # Otherwise, increment its priority
        else:
            AugHeapIncrementPriority(x.heap, x, 1)     # O(log n)
            
    def DEC_BIG_COUNT(self):
        ''' (OrderedWeightedSet) -> int
        Finds the key with the largest count, decrements that count, and 
        returns the key.  Returns False if all keys have count==0. '''
        
        # Get the heap
        heap = self.root.heap
        
        # Return false if all keys have count == 0
        # Keys are only added to the heap once their count is incremented to 1
        if len(heap) == 0 or AugHeapFindMax(heap).count == 0:   # O(1)
            return False
            
        # Get the top of the max-heap, which is the key with biggest count
        max = AugHeapExtractMax(heap)                           # O(log n)
        # Decrement the count for this key
        max.count -= 1
        # Re-insert the key into the heap if its count is > 0
        if max.count > 0:
            AugHeapInsert(heap, max)                            # O(log n)
        return max.key
        
        
        
# Heap Operations for CountingAVLNodes

def AugHeapInsert(H, node):
    H.append(node)                      # O(1)
    node.heapIndex = len(H) - 1
    AugHeapBubbleUp(H, node.heapIndex)  # O(log n), n is len(H)
    
def AugHeapBubbleUp(H, ind):
    ''' Uses node's "count" attribute as priority '''
    if ind == 0:
        return
    parent = (ind + 1) // 2 - 1
    if H[parent].count < H[ind].count:
        H[parent], H[ind] = H[ind], H[parent]
        H[ind].heapIndex = ind
        H[parent].heapIndex = parent
        AugHeapBubbleUp(H, parent)
        
def AugHeapIncrementPriority(H, node, inc):
    ''' (List<CountingAVLNode>, CountingAVLNode, int) -> None
    Increments the priority of the given node in the heap H by the given 
    integer inc
    Precondition: node.count + inc >= 0 '''
    node.count = node.count + inc
    if inc > 0:
        AugHeapBubbleUp(H, node.heapIndex)
    if inc < 0:
        AugHeapBubbleDown(H, node.heapIndex)

def AugHeapFindMax(H):
    return H[0]
    
def AugHeapExtractMax(H):
    H[0], H[-1] = H[-1], H[0]
    max = H.pop()
    AugHeapBubbleDown(H, 0)
    return max
    
def AugHeapBubbleDown(H, ind):
    left_child_i = (ind + 1) * 2 - 1
    right_child_i = (ind + 1) * 2
    # Check to see if children exist
    left_child_c = H[left_child_i].count if left_child_i < len(H) else -1
    right_child_c = H[right_child_i].count if right_child_i < len(H) else -1
    bigger_child_c = max(left_child_c, right_child_c)
    if H[ind].count >= bigger_child_c:
        return
    if left_child_c == bigger_child_c:
        H[ind], H[left_child_i] = H[left_child_i], H[ind]
        H[ind].heapIndex, H[left_child_i].heapIndex = ind, left_child_i
        AugHeapBubbleDown(H, left_child_i)
    elif right_child_c == bigger_child_c:
        H[ind], H[right_child_i] = H[right_child_i], H[ind]
        H[ind].heapIndex, H[right_child_i].heapIndex = ind, right_child_i
        AugHeapBubbleDown(H, right_child_i)
        
def AugHeapDecreasePriority(H, node, p)
        
if __name__ == "__main__":
    
    # Testing the OrderedWeightedSet
    
    # Instantiate ADT
    test = OrderedWeightedSet()
    
    # Add keys 0 thru 9
    for i in range(10):
        test.add(i)
    
    # Verify valid AVL tree:
    print("Printing Tree:")
    print_BST(test.root)
    print()
    
    # Increment each key's count to key value
    for i in range(10):
        for j in range(i):
            test.INC_COUNT(i)
    
    # Show current heap        
    print(test.heap)
    
    # Perform DEC_BIG_COUNT operations
    big = test.DEC_BIG_COUNT()
    print(big) # Expected: 9
    big = test.DEC_BIG_COUNT()
    print(big) # Expected: 8
    big = test.DEC_BIG_COUNT()
    print(big) # Expected: 9
    
    # Show current heap
    print(test.heap)
    
    # Increment count for key=6 twice
    test.INC_COUNT(6)
    test.INC_COUNT(6)
    big = test.DEC_BIG_COUNT()
    print(big) # Expected: 6
    
    # Show current heap
    print(test.heap)