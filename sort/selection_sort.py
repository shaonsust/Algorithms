"""
Python 3.8.2
Pure Python implementation of insertion sort.
Complexity O(n^2)
This algorithm will work on both float and integer type list.

Run this file for manual testing by following command:
python selection_sort.py

Tutorial link: https://www.geeksforgeeks.org/selection-sort/
"""


def selection_sort(arr):
    """
    Take a list for sorting.

    Args:
        collection (integer): It could be sorted or unsorted list.

    Returns:
        collection [integer]: A sorted list.

    Example:
    >>> selection_sort([5, 4, 6, 8 7 3])
    [3, 4, 5, 6, 7, 8]
    """

    length = len(arr)
    for i in range(length):  #Outer loop
        mn_pos = i

        for j in range(i, length): #Inner loop
            if arr[j] < arr[mn_pos]:
                mn_pos = j

        # Swaping here
        arr[i], arr[mn_pos] = arr[mn_pos], arr[i]

    return arr


if __name__ == "__main__":

    # Taking input from user to sort.
    USER_INPUT = [float(x) for x in input().split()]

    # Call selection sort to sort arr list.
    print(selection_sort(USER_INPUT))
