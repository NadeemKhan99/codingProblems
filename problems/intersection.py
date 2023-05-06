"""
Find the intersection of arrays
"""

from functools import reduce

def unique(arr1):
    """
    Return unique elements in an array
    """

    unique_array = []
    move = False
    length = 0

    for element in arr1:
        for unique in unique_array:
            if unique == element:
                move = True
                break
        if move:
            move = False
            continue
        unique_array.append(element)
        length += 1

    return (unique_array, length)


def intersection(arr1, arr2):
    """
    Calculating the intersection of 2 arrays
    """
    print(arr1, arr2)
    
    arr1, length1 = unique(arr1)
    arr2, length2 = unique(arr2)

    if length1 == 0:
        return arr2
    if length2 == 0:
        return arr1
    
    intersection_arr = []

    for element1 in arr1:
        is_exist = False
        for element2 in arr2:

            if element2 not in arr1 and element2 not in intersection_arr:
                intersection_arr.append(element2)
                continue
            
            if element1 == element2:
                is_exist = True
    
        if not is_exist:
            intersection_arr.append(element1)

    return intersection_arr


def advance_intersection(*args):
    """
    Calculating intersection of multiple arrays
    """
    return reduce(intersection, args)


advance_intersection([0,1,2,3,4,5],[0,1,99], [7,8,9,10])