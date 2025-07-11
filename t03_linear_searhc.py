
my_list = [1, 2, 3, 4, 5, 20, 30, 40, 51]


def linear_search(arr, target):
    """
    Perform linear search on the array to find the target value.
    Returns the index of the target if found, otherwise returns -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


# Example usage
target_values = [20, 23, 30, 40, 51, 100]

for target in target_values:
    index = linear_search(my_list, target)
    if index != -1:
        print(f"Value {target} found at index {index}.")
    else:
        print(f"Value {target} not found in the list.")
