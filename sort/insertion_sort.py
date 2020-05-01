"""
Python 3.8.2
Pure Python implementation of insertion sort.
Complexity O(n^2)
This algorithm will work on both float and integer type list.
"""


def insertion_sort(coll):
    """Sort an unsorted list by insertion sort algorithm."""
    for i in range(1, len(coll)):
        temp = coll[i]
        ptr = i - 1
        while temp < coll[ptr] and ptr >= 0:
            coll[ptr+1] = coll[ptr]
            ptr = ptr - 1
        coll[ptr + 1] = temp

    return coll


if __name__ == '__main__':
    USER_INPUT = [float(x) for x in input().split()]
    print(insertion_sort(USER_INPUT))
