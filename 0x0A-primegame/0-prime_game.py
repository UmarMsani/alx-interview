#!/usr/bin/python3

def is_prime(num):
    """
    Check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(n):
    """
    Generate a list of prime numbers up to n.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

def optimal_play(primes):
    """
    Determine the winner based on the number of primes available.
    """
    if len(primes) % 2 == 0:
        return "Ben"
    else:
        return "Maria"

def isWinner(x, nums):
    """
    Determine the winner of each round and overall winner.
    """
    winners = []
    for n in nums:
        primes = get_primes(n)
        winner = optimal_play(primes)
        winners.append(winner)
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
