from basics import searching
from basics import dataStructure
if __name__ == '__main__':
    test_array = [32,54,34,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_target = 3
    # test_search = searching.Search(test_array)
    # print(test_search.linear_search(test_target))
    # print(test_search.binary_search(test_target))
    
    array_test = dataStructure.Array()
    array_test.array_defination()
    
    for i in test_array:
        array_test.array_insert(i)

    array_test.array_trasverse()
    
    index_loc = array_test.array_search(3)
    print("\nindex of searched element :", index_loc)
    array_test.array_delete(index_loc)
    print("\nThe values in the array after deletion are:")
    array_test.array_trasverse()