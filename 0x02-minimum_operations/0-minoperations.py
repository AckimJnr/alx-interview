#!/usr/bin/python3
"""
module: 0-minoperations
"""


def minOperations(n):
    """
    Calculates minmum # of operations to be done
    to get n H chars
    """
    if n <= 0:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i

    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
