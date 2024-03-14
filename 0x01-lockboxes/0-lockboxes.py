#!/usr/bin/python3
"""
Contains a function for working on lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    boxes: list of lists or boxes to be opened
    """
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
