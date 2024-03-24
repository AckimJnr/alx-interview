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

    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    dp[2] = 2

    for i in range(3, n + 1):
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
