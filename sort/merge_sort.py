"""
This is the pure python implementation of merge sort.
Complexity O(nlog(n))
Python 3.8.2

Run this file by following command:
python merge_sort.py

Tutorial link: https://www.geeksforgeeks.org/merge-sort/
"""


def merge_sort(arr):
    """
    Taken an unsorted list and it will return a sorted list.

    Args:
        arr(integer): it could be sorted or unsorted list.

    Returns:
        arr(integer): return a sorted list.

    Example:
    >>> merge_sort([5, 4, 6, 2, 1, 3])
    [1, 2, 3, 4, 5, 6]
    """

    length = len(arr)
    if length <= 1:
        return arr

    mid = length // 2
    left = []
    right = []

    for i in range(mid):
        left.append(arr[i])

    for i in range(mid, length):
        right.append(arr[i])

    left = merge_sort(left)
    right = merge_sort(right)
    arr = merge(left, right)

    return arr


def merge(left, right):
    """
    Takes two sorted lists as two parameters and then merge it into one sorted list.

    Keyword Arguments:
        left(integer): sorted list
        right(integer): sorted list

    Returns:
        merge_arr(integer): Return a sorted merge list of two sorted list.
    """

    merged_arr = []
    l_s = 0
    r_s = 0
    l_l = len(left)
    r_l = len(right)

    while l_s < l_l and r_s < r_l:
        if left[l_s] < right[r_s]:
            merged_arr.append(left[l_s])
            l_s = l_s + 1
        else:
            merged_arr.append(right[r_s])
            r_s = r_s + 1

    if l_s == l_l:
        for i in range(r_s, r_l):
            merged_arr.append(right[i])
    else:
        for i in range(l_s, l_l):
            merged_arr.append(left[i])

    return merged_arr


if __name__ == '__main__':
    A = [int(x) for x in input().split()]
    A = merge_sort(A)
    print(A)
