"""
Python 3.8.2
Pure Python implementation of insertion sort.
Complexity O(n^2)
This algorithm will work on both float and integer type list.

Run this file for manual testing by following command:
python selection_sort.py
"""


def selection_sort(collection):
    """Take a list for sorting.

    Args:
        collection (integer): It could be sorted or unsorted list.

    Returns:
        collection [integer]: A sorted list.

    Example:
    >>> selection_sort([5, 4, 6, 8 7 3])
    [3, 4, 5, 6, 7, 8]
    """

    for i in enumerate(collection): #Outer loop
        mn_pos = i[0]
        for j in range(i[0], len(collection)): #Inner loop
            if collection[j] < collection[mn_pos]:
                mn_pos = j

        # Swaping here
        collection[i[0]], collection[mn_pos] = collection[mn_pos], collection[i[0]]

    return collection


if __name__ == "__main__":

    # Taking input from user to sort.
    USER_INPUT = [float(x) for x in input().split()]

    # Call selection sort to sort arr list.
    print(selection_sort(USER_INPUT))
