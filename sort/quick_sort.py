def quick_sort(a, start, end):
    if start < end:
        p_i = partition(a, start, end)
        a = quick_sort(a, start, p_i - 1)
        a = quick_sort(a, p_i + 1, end)

    return a

def partition(a, start, end):
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
