from tools import timed_step
from t03_linear_searhc import linear_search


def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the index of the target value.

    :param arr: List[int] - A sorted list of integers.
    :param target: int - The integer value to search for in the array.
    :return: int - The index of the target value in the array, or -1 if not found.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


long_list = [i for i in range(3000) if i % 3 == 0]

# Example usage
test_cases = [31, 100, 200, 500, 850, 999]
for target in test_cases:
    print("--------------")
    timed_step(f"Linear search for {target}", linear_search, long_list, target)
    timed_step(f"Binary search for {target}", binary_search, long_list, target)
