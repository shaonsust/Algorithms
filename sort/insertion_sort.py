"""
Python 3.8.2
Pure Python implementation of insertion sort.
Complexity O(n^2)
This algorithm will work on both float and integer type list.

Run this file for manual testing by following command:
python insertion_sort.py

Tutorial link: https://www.geeksforgeeks.org/insertion-sort/
"""


def insertion_sort(collection):
    """
    Take an unsorted list, then sorted it and return.

    Args:
        collection (integer): An unsorted or sorted list.

    Returns:
        collection (integer): A sorted list.

    Example:
    >>> insertion_sort([5, 4, 6, 8 7 3])
    [3, 4, 5, 6, 7, 8]
    """
    
    for i in range(1, len(collection)):
        for j in range(i, 0, -1):
            if collection[j] < collection[j-1]:
                collection[j], collection[j-1] = collection[j-1], collection[j]
            else:
                break
    return collection


if __name__ == '__main__':
    # Taking input from user.
    USER_INPUT = [float(x) for x in input().split()]

    # Call insertion sort for sorting and print it.
    print(insertion_sort(USER_INPUT))
