from tools import timed_step

"""
bubble sort = pairs of adjacent elements are compared, and the elements
swapped if they are not in order.

Quadratic time O(n^2)
small data set = okay-ish
large data set = BAD (plz don't)
"""


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                # Swap the elements
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


test_case = [9, 1, 8, 2, 7, 3, 6, 4, 5]

bubble_sort(test_case)

print("Sorted array:", test_case)

base_list = [1, 33, 121, 134, 18, 2, 89, 0, 3, 4, 5, 6, 7, 8, 110, 401, 19, 33, 41,
             12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             99, 123, 456, 789, 1000, 2000, 3000, 4000, 5000]
this_list = base_list.copy()
for i in range(10):
    this_list += [item * (i + 5) for item in base_list] + [item * (i + 3) for item in base_list]
    print("-----------")
    timed_step(f"Bubble sort step {i + 1}", bubble_sort, this_list)
    timed_step(f"Bubble sort step {i + 1} (sorted)", sorted, this_list)
