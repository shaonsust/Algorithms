"""
Python 3.8.2
Pure Python implementation of insertion sort.
Complexity O(n^2)
"""


def insertion_sort(coll):
    """[insersion sort method]

    Arguments:
        coll {[int]} -- [Coll is an unsorted list]
    """
    for i in range(1, len(coll)):
        temp = coll[i]
        ptr = i - 1
        while temp < coll[ptr] and ptr >= 0:
            coll[ptr+1] = coll[ptr]
            ptr = ptr - 1
        coll[ptr + 1] = temp

    return coll


if __name__ == '__main__':
    USER_INPUT = [int(x) for x in input().split()]
    print(insertion_sort(USER_INPUT))
