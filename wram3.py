'''
def find_duplicates(arr):
    """
    This function searches for duplicate entries in an input list of ints or strings and
    reports back all of the duplicates it finds.

    :param arr: The input list.
    :return: An output list containing all of the found duplicates within the input list.

    #>>> find_duplicates(['carrot', 'potato', 'carrot'])
    ['carrot']

    #>>> find_duplicates([1, 3, 5, 7, 3, 7, 10, 12, 12, 1, 8, 4])
    [1, 3, 7, 12]

    #>>> find_duplicates(['apple', 'kiwi', 'melon', 'dragonfruit', 'kiwi', 'lemon', 'melon', 'banana'])
    ['kiwi', 'melon']

    #>>> find_duplicates([1, 5, 5, -2, 5, 5, 2])
    [5]
    """

    result = []

    ##
    ## Your code here
    ##

    return sorted(result)
'''

def find_duplicates(arr):
    arr = sorted(arr)
    duplicate = []
    for el in arr:
        count = arr.count(el)
        if count > 1 and not el in duplicate:
            duplicate.append(el)
    print(duplicate)


find_duplicates(['carrot', 'potato', 'carrot'])
find_duplicates([1, 3, 5, 7, 3, 7, 10, 12, 12, 1, 8, 4])
find_duplicates(['apple', 'kiwi', 'melon', 'dragonfruit', 'kiwi', 'lemon', 'melon', 'banana'])
find_duplicates([1, 5, 5, -2, 5, 5, 2])
