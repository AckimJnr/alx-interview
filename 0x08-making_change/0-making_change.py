#!/usr/bin/python3
"""makeChange module"""


def makeChange(coins: int, total: int) -> int:
    """
    An algorithm calculating change give a pile of coins
    Args:
        coins: list of integers
        total: integer
    Returns:
        integer: minimum number of coins needed to make the total
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    coins = sorted(coins, reverse=True)

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
