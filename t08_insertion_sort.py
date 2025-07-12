from typing import List

from tools import timed_step

"""
Insertion sort = after comparing elements to the left,
shift elements to the right to make room to insert a value

Quadratic time O(n^2)
small data set = decent
large data set = BAD

Less steps than Bubble sort
Best case is O(n) compared to Selection sort O(n^2)
"""


def insertion_sort(array: List[int]) -> List[int]:
    """ Sorts an array in-place using the insertion sort algorithm.
        Returns the same array sorted in ascending order.
    """
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


test_case = [9, 1, 8, 2, 7, 3, 6, 4, 5]

insertion_sort(test_case)

print("Sorted array:", test_case)

base_list = [1, 33, 121, 134, 18, 2, 89, 0, 3, 4, 5, 6, 7, 8, 110, 401, 19, 33, 41,
             12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             99, 123, 456, 789, 1000, 2000, 3000, 4000, 5000]
this_list = base_list.copy()
for i in range(10):
    this_list += [item * (i + 5) for item in base_list] + [item * (i + 3) for item in base_list]
    print("-----------")
    timed_step(f"Insertion sort step {i + 1}", insertion_sort, this_list)
    timed_step(f"-Sorted- sort step {i + 1}", sorted, this_list)
