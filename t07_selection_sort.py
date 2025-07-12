from typing import List

from tools import timed_step

"""
selection_sort: Search through an array and keep track of the minimum value during
each iteration. At the end of each iteration, we swap values.

Quadratic time O(n^2)
small data set = okay
large data set = BAD
"""


def selection_sort(array: List[int]) -> List[int]:
    """Sorts an array in-place using the selection sort algorithm.
    Returns the same array sorted in ascending order.
    """
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    return array


test_case = [9, 1, 8, 2, 7, 3, 6, 4, 5]

selection_sort(test_case)

print("Sorted array:", test_case)

base_list = [1, 33, 121, 134, 18, 2, 89, 0, 3, 4, 5, 6, 7, 8, 110, 401, 19, 33, 41,
             12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             99, 123, 456, 789, 1000, 2000, 3000, 4000, 5000]
this_list = base_list.copy()
for i in range(10):
    this_list += [item * (i + 5) for item in base_list] + [item * (i + 3) for item in base_list]
    print("-----------")
    timed_step(f"Selection sort step {i + 1}", selection_sort, this_list)
    timed_step(f"-Sorted- sort step {i + 1}", sorted, this_list)
