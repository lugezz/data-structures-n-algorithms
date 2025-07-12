from tools import timed_step

"""
merge sort = recursively divide array in 2, sort, re-combine
run-time complexity = O(n Log n)
space complexity    = O(n)
"""


def merge(left, right):
    """ Merges two sorted arrays into one sorted array. """
    sorted_array = []
    left_index, right_index = 0, 0

    # Compare elements from both halves and merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    # Append any remaining elements from both halves
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])

    return sorted_array


def merge_sort(arr):
    """ Sorts an array using the merge sort algorithm. """
    # Base case: if the array is of length 0 or 1, it is already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


test_case = [9, 1, 8, 2, 7, 3, 6, 4, 5]

merge_sort(test_case)

print("Sorted array:", test_case)

base_list = [1, 33, 121, 134, 18, 2, 89, 0, 3, 4, 5, 6, 7, 8, 110, 401, 19, 33, 41,
             12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             99, 123, 456, 789, 1000, 2000, 3000, 4000, 5000]
this_list = base_list.copy()
for i in range(10):
    this_list += [item * (i + 5) for item in base_list] + [item * (i + 3) for item in base_list]
    print("-----------")
    timed_step(f"Merge sort step {i + 1}", merge_sort, this_list, print_results=False)
    timed_step(f"-Sorted- sort step {i + 1}", sorted, this_list, print_results=False)
