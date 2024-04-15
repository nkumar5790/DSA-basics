import numpy as np 

class Search:
    def __init__(self, array ):
        self.array = array
        self.size = len(array)
        
    def linear_search(self, target):
        if  not self.array:
            return -1
        for i in range(self.size):
            if self.array[i] == target:
                return i
        return -1
    
    def binary_search(self,target):
        if not self.array :
            return -1
        sorted_array = np.sort(self.array)
        low = 0
        max = self.size
        mid = (low + max) // 2
        while sorted_array[mid]!= target:
            if sorted_array[mid] > target:
                max = mid - 1
            else:
                low = mid + 1
            mid = (low + max) // 2
            if low > max:
                return -1
        return sorted_array[mid]