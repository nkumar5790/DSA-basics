'''This is file which holds all the major Data Structures used in the project
those are:
1. Array
2. Stack
3. Queue
4. Linked List
5. Binary Tree
6. Graph
7. Heap
8. Trie
9. Hash Table
10. Priority Queue
11. Disjoint Set
12. AVL Tree
''' 

class Array:
    '''This is a class for the array data structure'''
    def __init__(self):
        self.array = [] 
        self.length = 0
    def array_defination(self,):
        print ("""
        Array is type of data structure which is used to store data in a sequential manner.
        The array is a collection of elements of the same type.The elements are stored in a contiguous block of memory.
        The elements of the array can be accessed using the index of the element.
        
        Basic terminology :
        1. array_index : The index of an element in an array.
        2. array_length : The number of elements in an array.
        3. array_element : The value of an element in an array.
        4. array_capacity : The maximum number of elements that can be stored in an array.
        
        Types of array:
        1. One Dimensional Array : An array that has only one dimension. Example: [1,2,3,4,5]
        2. Multi Dimensional Array : An array that has more than one dimension. Example: [[1,2,3],[4,5,6],[7,8,9]]
        3. Static Array : An array that has fixed size. Example: [1,2,3,4,5,6,7,8,9,10]
        4. Dynamic Array : An array that can grow and shrink as needed. Example: []
        
        Advantages of Array:
        1. Arrays allow random access to elements. This makes accessing elements by position faster.
        2. Arrays have better cache locality which makes a pretty big difference in performance.
        3. Arrays represent multiple data items of the same type using a single name.
        4. Arrays are used to implement the other data structures like linked lists, stacks, queues, trees, graphs, etc.

        Disadvantages of Array:
        1. As arrays have a fixed size, once the memory is allocated to them, it cannot be increased or decreased, making it impossible to store extra data if required. An array of fixed size is referred to as a static array. 
        2. Allocating less memory than required to an array leads to loss of data.
        3. An array is homogeneous in nature so, a single array cannot store values of different data types. 
        4. Arrays store data in contiguous memory locations, which makes deletion and insertion very difficult to implement. This problem is overcome by implementing linked lists, which allow elements to be accessed sequentially.  
        
        references_link:
        https://www.geeksforgeeks.org/introduction-to-arrays-data-structure-and-algorithm-tutorials/?ref=next_article
        """)
    def array_insert(self,value):
        """This function is used to insert the value in the array"""
        self.array.append(value)
        self.length += 1
        
    def array_trasverse(self,print_val=False):
        """This function is used to traverse the array and extract the values"""

        if print_val:
            print("The values in the array are:")
            for i in range(self.length):
                print(self.array[i])
        print("The length of the array is:",self.length)
        print("The capacity of the array is:",len(self.array))
        print("The array is:",self.array)
        
    def array_search(self,value):
        """This function is used to search the value in the array"""
        for i in range(self.length):
            if self.array[i] == value:
                return i
        return -1
    
    def array_delete(self,index):
        """This function is used to delete the value from the array"""
        if index >= self.length:
            print("Index out of bound , No element to delete ")
            return 
        if index < 0:
            print( "Index out of bound , No element to delete ")
            return 
        self.array.pop(index)
        self.length -= 1
    
class Stack:
    """This is a class for the stack data structure"""
    def __init__(self):
        self.stack = []
        self.length = 0
        
    def stack_defination(self):
        print("""
        Stack is a linear data structure that stores items in a Last In First Out (LIFO) manner.
        The name Stack is derived from the analogy of a set of physical items stacked on top of each other,
        which makes it easy to take an item off the top of the stack, while getting to an item deeper in the stack may require taking off multiple other items first.
        """)
    def stack_push(self,value):
        """This function is used to push the value in the stack"""
        self.stack.append(value)
        self.length += 1
        
    def stack_pop(self):
        """This function is used to pop the value from the stack"""
        if self.length == 0:
            print("Stack is empty, No element to pop")
            return
        self.stack.pop()
        self.length -= 1
    
    def stack_peek(self):
        """This function is used to peek the value from the stack"""
        if self.length == 0:
            print("Stack is empty, No element to peek")
            return
        print("The top element of the stack is:",self.stack[-1])
        
    def stack_is_empty(self):
        """This function is used to check if the stack is empty"""
        if self.length == 0:
            return True
        return False
    
    def stack_is_full(self):
        """This function is used to check if the stack is full"""
        if self.length == len(self.stack):
            return True
        return False
    
    def stack_search(self,value):
        """This function is used to search the value in the stack"""
        for i in range(self.length):
            if self.stack[i] == value:
                return i
        return -1
    
    def reverse_stack(self):
        """This function is used to reverse the stack"""
        self.stack = self.stack[::-1]
        
class Queue:
    """This is a class for the queue data structure"""
    def __init__(self):
        self.queue = []
        self.length = 0

    def queue_defination(self):
        print("""
        Queue is a linear data structure that stores items in a First In First Out (FIFO) manner.
        The name Queue is derived from the first person to arrive who is first served.
        """)
        
    def enqueue(self,value):
        """This function is used to enqueue the value in the queue"""
        self.queue.append(value)
        self.length += 1
        
    def deque(self):
        """This function is used to dequeue the value from the queue"""
        if self.length == 0:
            print("Queue is empty, No element to dequeue")
            return
        self.queue.pop(0)
        self.length -= 1
        
    def queue_peek(self):
        """This function is used to peek the value from the queue"""
        if self.length == 0:
            print("Queue is empty, No element to peek")
            return
        print("The front element of the queue is:",self.queue[0])
        return self.queue[0]
        
    def queue_is_empty(self):
        """This function is used to check if the queue is empty"""
        if self.length == 0:
            return True
        return False
    
    def queue_is_full(self):
        """This function is used to check if the queue is full"""
        if self.length == len(self.queue):
            return True
        return False
    
    def queue_search(self,value):
        """This function is used to search the value in the queue"""
        for i in range(self.length):
            if self.queue[i] == value:
                return i
        return -1
    
    def reverse_queue(self):
        """This function is used to reverse the queue"""
        self.queue = self.queue[::-1]
        
    def circular_queue(self):
        """This function is used to implement a circular queue"""
        if self.length == 0:
            print("Queue is empty, No element to reverse")
            return
        self.queue = self.queue[1:] + self.queue[:1]
        
    def circular_queue_peek(self):
        """This function is used to peek the value from the circular queue"""
        if self.length == 0:
            print("Queue is empty, No element to peek")
            return
        print("The front element of the queue is:",self.queue[0])
        return self.queue[0]
        
    

class LinkedList:
    """This is a class for the linked list data structure"""
    def __init__(self):
        self.head = None
        self.length = 0
        
    def linked_list_defination(self):
        print("""
        Linked List is a linear data structure that stores items in a non-contiguous manner.
        Each element in a linked list is called a node. Each node has two components:
        1. Data: The value of the node.
        2. Next: The reference to the next node in the linked list.
        The first node in the linked list is called the head.
        The last node in the linked list has a reference to None.
        Example:
        The following is a linked list:
        1->2->3->4->5->None
        """)
class LinklistNode:
    """This is a class for the node of the linked list data structure"""
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def linked_list_node_defination(self):
        print("""
        Linked List Node is a data structure that stores the value of the node and the reference to the next node.
        """)
    
    def linked_list_node_insert(self,value):
        """This function is used to insert the value in the linked list"""
        self.next = LinklistNode(value)
    
    def linked_list_node_delete(self):
        """This function is used to delete the node from the linked list"""
        self.value = None
        self.next = None
    
    def linked_list_node_search(self,value):
        """This function is used to search the value in the linked list"""
        if self.value == value:
            return True
        if self.next == None:
            return False
        return self.next.linked_list_node_search(value)
    
    def linked_list_node_traverse(self):
        """This function is used to traverse the linked list"""
        print("The value of the node is:",self.value)
        if self.next != None:
            self.next.linked_list_node_traverse()
    
    def linked_list_node_reverse(self):
        """This function is used to reverse the linked list"""
        prev = None
        current = self
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self = prev
        return self
    
    def linked_list_node_circular(self):
        """This function is used to implement a circular linked list"""
        if self.next == None:
            self.next = self
        else:
            self.next = self.next.linked_list_node_circular()
            return self
        return self
    
    def linked_list_node_circular_peek(self):
        """This function is used to peek the value from the circular linked list"""
        if self.next == None:
            print("Queue is empty, No element to peek")
            return
        print("The front element of the queue is:",self.next.value)
        return self.next.value
    
    def linked_list_node_circular_delete(self):
        """This function is used to delete the node from the circular linked list"""
        self.value = None
        self.next = None
        return self
    
    def linked_list_node_circular_search(self,value):
            """This function is used to search the value in the circular linked list"""
            if self.value == value:
                return True
            if self.next == None:
                return False
            return self.next.linked_list_node_circular_search(value)
    
    def linked_list_node_circular_reverse(self):
            """This function is used to reverse the circular linked list"""
            prev = None
            current = self
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            self = prev
            return self
    
class DoublyLinkedList:
    """This is a class for the doubly linked list data structure"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def doubly_linked_list_defination(self):
        print("""
        Doubly Linked List is a linear data structure that stores items in a non-contiguous manner.
        Each element in a doubly linked list is called a node. Each node has three components:
        1. Data: The value of the node.
        2. Previous: The reference to the previous node in the doubly linked list.
        3. Next: The reference to the next node in the doubly linked list.
        The first node in the doubly linked list is called the head.
        The last node in the doubly linked list has a reference to None.
        Example:
        The following is a doubly linked list:
        1->2->3->4->5->None
        """)
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def doubly_linked_list_insert(self,value):
        """This function is used to insert the value in the doubly linked list"""
        new_node = LinklistNode(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
    
    def doubly_linked_list_delete(self):
        """This function is used to delete the node from the doubly linked list"""
        if self.head == None:
            print("The linked list is empty, No element to delete")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            
    def doubly_linked_list_search(self,value):
        """This function is used to search the value in the doubly linked list"""
        if self.head == None:
            print("The linked list is empty, No element to search")
            return
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def doubly_linked_list_traverse(self):
        """This function is used to traverse the doubly linked list"""
        if self.head == None:
            print("The linked list is empty, No element to traverse")
            return
        current = self.head
        while current:
            print("The value of the node is:",current.value)
            current = current.next
    
    def doubly_linked_list_reverse(self):
        """This function is used to reverse the doubly linked list"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self.head
    
    def doubly_linked_list_circular_defination(self):
        print("""
        Circular Doubly Linked List is a doubly linked list in which all nodes are connected to form a circle.
        The last node points to the first node.
        The first node points to the last node.
        Example:
        The following is a circular doubly linked list:
        1->2->3->4->5->1->2->3->4->5->1->2->3->4->5->None
        """)
        
    
    
class BinaryTree:
    """This is a class for the binary tree data structure"""
    def __init__(self):
        self.root = None
        
    def binary_tree_defination(self):
        print("""
        Binary Tree is a hierarchical data structure in which each node has at most two children, referred to as the left child and the right child.
        The topmost node in the tree is called the root. The nodes that have no children are called leaves.
        The height of a binary tree is the maximum depth of the tree.
        The depth of a node is the number of edges from the root to the node.
        The height of a binary tree is the maximum depth of the tree.
        The depth of a node is the number of edges from the root to the node.
        EXAMPLE:
        The following is a binary tree:
        1
        / \
        2   3
        / \
        4   5
        """)
class BTreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def binary_tree_insert(self,value):
        """This function is used to insert the value in the binary tree"""
        if value < self.value:
            if self.left == None:
                self.left = BTreeNode(value)
            else:
                self.left.binary_tree_insert(value)
                
    def binary_tree_search(self,value):
        """This function is used to search the value in the binary tree"""
        if value == self.value:
            return True
        if value < self.value:
            if self.left == None:
                return False
            return self.left.binary_tree_search(value)
        if value > self.value:
            if self.right == None:
                return False
            return self.right.binary_tree_search(value)
    
    def binary_tree_traverse(self):
        """This function is used to traverse the binary tree"""
        if self.left:
            self.left.binary_tree_traverse()
        print("The value of the node is:",self.value)
        if self.right:
            self.right.binary_tree_traverse()
    
    def binary_tree_delete(self,value):
        """This function is used to delete the value from the binary tree"""
        if value < self.value:
            if self.left:
                self.left = self.left.binary_tree_delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.binary_tree_delete(value)
        else:
            if self.left == None:
                return self.right
            elif self.right == None:
                return self.left
            min_value = self.right.binary_tree_min()
            self.value = min_value
            self.right = self.right.binary_tree_delete(min_value)
        return self
    
    def binary_tree_min(self):
        """This function is used to find the minimum value in the binary tree"""
        if self.left == None:
            return self.value
        return self.left.binary_tree_min()
    
    def binary_tree_max(self):
        """This function is used to find the maximum value in the binary tree"""
        if self.right == None:
            return self.value
        return self.right.binary_tree_max()
    
    def binary_tree_height(self):
        """This function is used to find the height of the binary tree"""
        if self.left == None and self.right == None:
            return 0
        if self.left == None:
            return 1 + self.right.binary_tree_height()
        if self.right == None:
            return 1 + self
    
    def binary_tree_depth(self):
        """This function is used to find the depth of the binary tree"""
        if self.left == None and self.right == None:
            return 0
        if self.left == None:
            return 1 + self.right.binary_tree_depth()
        if self.right == None:
            return 1 + self.left.binary_tree_depth()
    
        
class Graph:
    """This is a class for the graph data structure"""
    def __init__(self):
        self.graph = {}

    def graph_defination(self):
        print("""
        Graph is a pictorial representation of a set of objects where some pairs of objects are connected by links.
        The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges.
        The various ways in which pairs of vertices may be connected by edges without forming loops are termed as graphs.
        The graph can be represented in various ways, such as:
        Adjacency Matrix: A two-dimensional array of nodes and the links between them.
        Adjacency List: A collection of linked lists, one for each vertex.
        Adjacency Matrix and Adjacency List are both linear data structures.
        Adjacency Matrix is used to represent weighted graphs, while Adjacency List is used to represent unweighted graphs.
        Adjacency Matrix is used to represent directed graphs, while Adjacency List is used to represent undirected graphs.
        Adjacency Matrix is used to represent graphs with more than 1000 vertices, while Adjacency List is used to represent graphs with less than 1000 vertices.
        Example:
        Graph:
        A----B
        |    |
        C----D
        """)
        
class Heap:
    """This is a class for the heap data structure"""
    def __init__(self):
        self.heap = []
        self.length = 0

    def heap_defination(self):
        print("""
        Heap is a special tree-based data structure which is essentially a complete binary tree.
        The difference between a Binary Heap and a Binary Search Tree is that a Binary Heap is a Min Heap while a Binary Search Tree is a Max-Heap.
        The Min Heap property states that the key (the value) in a node must be less than or equal to the keys in all of its children.
        The Max Heap property states that the key (the value) in a node must be greater than or equal to the keys in all of its children.
        Heaps are often implemented with an array.
        Example:
        Min Heap:
        10
        20
        30
        40
        50
        Max Heap:
        50
        40
        30
        20
        10
        """)
class Trie:
    """This is a class for the trie data structure"""
    def __init__(self):
        self.trie = {}
        self.length = 0
    
    def trie_defination(self):
        print("""
        Trie is a tree-like data structure that stores a dynamic set of strings.
        Tries are used to search for strings in a dataset. They are efficient in searching for strings in a dataset.
        Tries are used to store strings in a dataset. They are efficient in storing strings in a dataset.
        Tries are used to check if a string is present in a dataset. They are efficient in checking if a string is present in a dataset.
        Tries are used to retrieve all the strings that have a common prefix. They are efficient in retrieving all the strings that have a common prefix.
        Example:
        Trie:
        root
        /   \
        a     b
        / \   / \
        c   d e   f
        / \
        g   h
        """)

class HashTable:
    """This is a class for the hash table data structure"""
    def __init__(self):
        self.hash_table = {}
        self.length = 0
        
    def hash_table_defination(self):
        print("""
        Hash Table is a data structure that stores key-value pairs.
        The keys are unique and used to retrieve the values.
        The hash function is used to compute the index of the key-value pair in the hash table.
        Example:
        Hash function: h(key) = key % 10
        """)
        
class PriorityQueue:
    """This is a class for the priority queue data structure"""
    def __init__(self):
        self.priority_queue = []
        self.length = 0

    def priority_queue_defination(self):
        print("""
        Priority Queue is a data structure that stores a collection of elements.
        The elements are ordered based on their priority.
        The highest priority element is at the front of the queue.
        The lowest priority element is at the rear of the queue.
        Example:
        Priority Queue:
        [1,2,3,4,5]
        """)

class DisjointSet:
    """This is a class for the disjoint set data structure"""
    def __init__(self):
        self.disjoint_set = {}
        self.length = 0
    
    def disjoint_set_defination(self):
        print("""
        Disjoint Set is a data structure that stores a collection of elements.
        The elements are grouped into disjoint sets.
        The disjoint sets are represented by a collection of trees.
        The disjoint sets are used to check if two elements are in the same set.
        The disjoint sets are used to merge two sets into one.
        Example:
        Disjoint Set:
        {1,2,3,4,5}
        """)

class AVLTree:
    """This is a class for the AVL tree data structure"""
    def __init__(self):
        self.avl_tree = {}
        self.length = 0

    def avl_tree_defination(self):
        print("""
        AVL Tree is a self-balancing Binary Search Tree (BST).
        The heights of the two child subtrees of any node differ by at most one;
        left subtree's height >= right subtree's height.
        AVL Tree is a special type of Binary Search Tree in which the difference between the heights of left and right subtrees cannot be more than one for all nodes.
        Example:
        AVL Tree:
        root
        /   \
        a     b
        / \   / \
        c   d e   f
        / \
        g   h
        """)
    