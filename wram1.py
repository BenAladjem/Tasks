def find_largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(max)

    """
    This function should find the largest element in the input list and return it.

    :param arr: A list of integers.
    :return: The largest element in arr.

    >>> find_largest([1, 22, 55, 90])
    90

    >>> find_largest([0, 0, -1, -20, 0, -20])
    0

    >>> find_largest([-25, -100, -5, -22, -50])
    -5

    >>> find_largest(['A', 'B', 'C', 'D', 'E'])
    'E'
    """

find_largest([1, 22, 55, 90])
find_largest([0, 0, -1, -20, 0, -20])
find_largest([-25, -100, -5, -22, -50])
find_largest(['A', 'B', 'C', 'D', 'E'])