#!/usr/bin/python3
""" Make change module """


def makeChange(coins, total):
    """
    determines the fewest coins to meet total

    Args:
        coins: an array of coins
        total: total to be met

    Return:
        Total coins
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else - 1
