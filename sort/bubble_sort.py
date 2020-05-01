"""
Python 3.8.2
Pure Python Implementation of Bubble sort algorithm
Complexity is O(n^2)
This algorithm will work on both float and integer type list.
"""


def bubble_sort(arr):
    """Sorting array with bubble sort algorithm"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] # Swaping here

    return arr


if __name__ == '__main__':

    # Taking input from user
    USER_INPUT = [float(x) for x in input().split()]

    # call bublesort to sort an unsorted list.
    print(bubble_sort(USER_INPUT))
