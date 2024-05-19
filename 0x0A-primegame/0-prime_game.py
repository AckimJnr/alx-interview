#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determines the winner based on the given integer and list of integers.
    Args:
        x (int): number of rounds
        nums (list): list of integers
    Returns:
        str: Name of the winner (Maria or Ben) or None if no winner.
    """
    if not nums or x < 1:
        return None

    n = max(nums)

    # Sieve of Eratosthenes
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not primes
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Cumulative count of primes up to each index
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime[i] else 0)

    maria_wins = 0

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1

    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x / 2:
        return "Ben"
    else:
        return None
