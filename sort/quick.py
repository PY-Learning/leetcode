#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quick(L, low, high):
    """quick sort.

    :L: array[int]
    :low: begin index
    :high: end index
    :returns: array[int]
    """
    i, j = low, high
    if i >= j: return L

    key = L[i]
    while i < j:
        while (i < j) and (L[j] >= key):
            j -= 1
        L[i] = L[j]
        while (i < j) and (L[i] <= key):
            i += 1
        L[j] = L[i]
    L[i] = key
    quick(L, low, i-1)
    quick(L, j+1, high)
    return L




if __name__ == "__main__":
    test_data = [10, 5, 1, 4, 8, 6, 7, 12, 7]
    print(quick(test_data, 0, len(test_data)-1))
