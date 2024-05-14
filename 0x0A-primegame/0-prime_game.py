#!/usr/bin/python3
"""Prime Game task 0. Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner of each round and overall winner.
    """
    # invalid input checks
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    # initialize scores and array of possible prime nums.
    ben = 0
    maria = 0
    # Toh Create list 'a' of length sorted(nums)[-1] + 1 with all element.
    # set to 1.
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    # The first two elements of the list, a[0] and a[1], are set to 0.
    a[0], a[1] = 0, 0
    # sieve of Eratosthenes algorithm to generate array of prime nums.
    for i in range(2, len(a)):
        rm_multiples(a, i)
    # Will play each round of the game
    for i in nums:
        # If the sum of prime numbers in the set is even, Ben wins.
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine the winner of the game.
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    remove multiples of prime number from an array of possible prime
    nums.

    Args:
        ls (list of int): An array of possible prime numbers.
        x (int): The prime number to remove multiples of.

    Returns: None.

    Raises: None.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
