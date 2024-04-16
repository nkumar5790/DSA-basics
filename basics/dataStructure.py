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
    
    