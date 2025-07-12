from tools import timed_step
from t03_linear_searhc import linear_search


"""
improvement over binary search best used for "uniformly" distributed data
"guesses" where a value might be based on calculated probe results
if probe is incorrect, search area is narrowed, and a new probe is calculated
"""


def interpolation_search(arr, target):
    """
    Perform interpolation search on a sorted array to find the index of the target value.

    :param arr: List[int] - A sorted list of integers.
    :param target: int - The integer value to search for in the array.
    :return: int - The index of the target value in the array, or -1 if not found.
    """
    low, high = 0, len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Calculate the probe position
        probe = low + (high - low) * (target - arr[low]) // (arr[high] - arr[low])

        if arr[probe] == target:
            return probe
        elif arr[probe] < target:
            low = probe + 1
        else:
            high = probe - 1

    return -1


long_list = [i for i in range(3000) if i % 3 == 0]

# Example usage
test_cases = [31, 100, 200, 500, 850, 999]
for target in test_cases:
    print("--------------")
    timed_step(f"Linear search for {target}", linear_search, long_list, target)
    timed_step(f"Binary search for {target}", interpolation_search, long_list, target)
