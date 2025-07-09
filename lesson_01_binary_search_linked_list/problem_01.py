from tools import timed_step_check

"""
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in
decreasing order, and lays them out face down in a sequence on a table. She challenges Bob
to pick out the card containing a given number by turning over as few cards as possible.
Write a function to help Bob locate the card.
"""


def base_locate_card(cards, query):
    if not cards:
        # If the list is empty, return -1
        return -1

    # Create a variable position with the value 0
    position = 0

    # Set up a loop for repetition
    while True:
        # Check if element at the current position matche the query
        if cards[position] == query:
            # Answer found! Return and exit..
            return position

        # Increment the position
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):

            # Number not found, return -1
            return -1


def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


test_cases = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
]

for test in test_cases:
    timed_step_check(
        f"locate_card({test['input']['cards']}, {test['input']['query']})",
        locate_card,
        test['output'],
        **test['input']
    )
