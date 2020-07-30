"""
Python 3.8.2
Pure Python Implementation of Bubble sort algorithm
Complexity is O(n^2)
This algorithm will work on both float and integer type list.

Run this file for manual testing by following command:
python bubble_sort.py
"""


def bubble_sort(arr):
    """
    Take an unsorted list and return a sorted list.

    Args:
        arr (integer) -- it could be sorted or unsorted list.

    Returns:
        arr (integer) -- A sorted list.

    Example:
    >>> bubble_sort([5, 4, 6, 8 7 3])
    [3, 4, 5, 6, 7, 8]
    """

    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swaping here

    return arr


if __name__ == '__main__':
    # Taking input from user
    USER_INPUT = [float(x) for x in input().split()]

    # call bublesort to sort an unsorted list and print it.
    print(bubble_sort(USER_INPUT))
