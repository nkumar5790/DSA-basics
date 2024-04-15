from basics import searching

if __name__ == '__main__':
    test_array = [32,54,34,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    test_target = 3
    test_search = searching.Search(test_array)
    print(test_search.linear_search(test_target))
    print(test_search.binary_search(test_target))