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
