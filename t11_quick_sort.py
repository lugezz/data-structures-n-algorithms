from tools import timed_step

"""
quick sort = moves smaller elements to left of a pivot.
recursively divide array in 2 partitions

run-time complexity = Best case O(n log(n))
Average case O(n log(n))
Worst case O(n^2) if already sorted
space complexity    = O(log(n)) due to recursion
"""


def partition(arr, low, high):
    """ Helper function to partition the array around a pivot. """
    # Choose the last element as pivot
    pivot = arr[high]
    # Pointer for the smaller element
    i = low - 1

    for j in range(low, high):
        # If current element is smaller than pivot
        if arr[j] < pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    # Return the index of the pivot
    return i + 1


def quick_sort(arr, low: int = None, high: int = None):
    """ Sorts an array using the quick sort algorithm. """
    if low is None or high is None:
        # Initialize low and high if not provided
        low, high = 0, len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)  # Partitioning index

        # Recursively sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr


test_case = [9, 1, 8, 2, 7, 3, 6, 4, 5]

quick_sort(test_case)

print("Sorted array:", test_case)

base_list = [1, 33, 121, 134, 18, 2, 89, 0, 3, 4, 5, 6, 7, 8, 110, 401, 19, 33, 41,
             12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
             99, 123, 456, 789, 1000, 2000, 3000, 4000, 5000]
this_list = base_list.copy()
for i in range(10):
    this_list += [item * (i + 5) for item in base_list] + [item * (i + 3) for item in base_list]
    print("-----------")
    timed_step(f"Quick sort step {i + 1}", quick_sort, this_list, print_results=False)
    timed_step(f"-Sorted- sort step {i + 1}", sorted, this_list, print_results=False)
