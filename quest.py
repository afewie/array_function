def filter_greater(arr, value):
    new_lst = []
    
    for elem in arr:
        if elem > value:
            new_lst.append(elem)
    return new_lst

def filter_less(arr, value):
    new_lst = []
    
    for elem in arr:
        if elem < value:
            new_lst.append(elem)
    return new_lst

def filter_equal(arr, value):
    new_lst = []
    
    for elem in arr:
        if elem == value:
            new_lst.append(elem)
    return new_lst
def filter_not_equal(arr, value):
    new_lst = []
    
    for elem in arr:
        if elem != value:
            new_lst.append(elem)
    return new_lst

def test_funtcion():
    actual = filter_greater([1, 5, 2, 8, 3, 9, 4, 7, 6], 5)
    print(actual)

    actual1 = filter_less([1, 5, 2, 8, 3, 9, 4, 7, 6], 5)
    print (actual1)

    actual2 = filter_equal([1, 5, 2, 8, 3, 9, 4, 7, 6], 5)
    print(actual2)

    actual3 = filter_not_equal([1, 5, 2, 8, 3, 9, 4, 7, 6], 5)
    print(actual3)
