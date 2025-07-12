"""
Hanoi Tower Problem
This code implements the solution to the Tower of Hanoi problem using recursion.
It defines a function to move disks from one peg to another, and a function to solve the
problem by moving all disks from the source peg to the destination peg using an auxiliary peg.
"""


def hanoi_tower(n: int, source: str = "A", destination: str = "B", auxiliary: str = "C"):
    """
    Move n disks from source peg to destination peg using auxiliary peg.

    :param n: Number of disks
    :param source: Name of the source peg
    :param destination: Name of the destination peg
    :param auxiliary: Name of the auxiliary peg
    """
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    hanoi_tower(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi_tower(n - 1, auxiliary, destination, source)


# A is source, C is destination, B is auxiliary
# Example output for 3 disks:
hanoi_tower(3)
print("-" * 100)

# Example output for 5 disks:
hanoi_tower(5)
