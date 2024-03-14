#!/usr/bin/python3
"""
Contains a function for working on lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    boxes: list of lists representing boxes to be opened
            where each box contains a list of keys that can open it.
    """
    if not isinstance(boxes, list):
        return False

    if not boxes:
        return True

    n = len(boxes)
    visited = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < n:
                queue.append(key)
    return len(visited) == n
