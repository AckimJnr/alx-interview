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
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order

    num_coins = 0
    remaining_total = total

    for coin in coins:
        if coin <= remaining_total:
            num_coins += remaining_total // coin
            remaining_total %= coin
            if remaining_total == 0:
                return num_coins

    return -1
