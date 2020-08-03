"""
This is the pure python implementation of quick sort.
Best Complexity is O(nlog(n)).
Python 3.8.2

Run this file by following command:
python quick_sort.py

Tutorial link: https://www.geeksforgeeks.org/quick-sort/
"""


def quick_sort(a, start, end):
    """
    Quick sort algorithm.

    Args:
        a (int): unsorted list.
        start (int): start index of list a.
        end (int): end index of list a.

    Returns:
        a (int): will return sorted list.
    """
    if start < end:
        p_i = partition(a, start, end)
        a = quick_sort(a, start, p_i - 1)
        a = quick_sort(a, p_i + 1, end)

    return a

def partition(a, start, end):
    """
    This function will let pivot as last element of the list.
    All smaller element than pivot will place in the left side of the pivot
    and greater element than pivot will place in the right side of the pivot.
    And pivot itself will place as its correct position. At last this function will return
    index of pivot's correct position.

    Args:
        a (int): an unsorted list.
        start (int): start point
        end (int): End Point.

    Returns:
        p_i (int): return pivot index.

    Example:
    >>> quick_sort([5, 4, 6, 2, 1, 3])
    [1, 2, 3, 4, 5, 6]
    """
    p_i = start
    pivot = a[end]
    for i in range(start, end):
        if a[i] <= pivot:
            a[i], a[p_i] = a[p_i], a[i]
            p_i += 1

    a[p_i], a[end] = a[end], a[p_i]

    return p_i


if __name__ == '__main__':
    USER_INPUT = [float(x) for x in input().split()]
    print(quick_sort(USER_INPUT, 0, len(USER_INPUT) - 1))
