"""
Python version: 3.8.2
This is pure python implementation of selection sort.
Complexity is O(n^2)
This algorithm will work on both float and integer type list.
"""


def selection_sort(collection):
    """Sort a list by selection sort"""
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
