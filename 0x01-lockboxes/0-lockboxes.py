#!/usr/bin/python3

def canUnlockAll(boxes):
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    if n == 0:
        return False

    # Set to keep track of opened boxes
    opened_boxes = set()

    # Initialize with the first box (index 0)
    opened_boxes.add(0)

    # Queue to keep track of keys to explore
    keys_to_explore = boxes[0]

    while keys_to_explore:
        key = keys_to_explore.pop(0)

        if key < n and key not in opened_boxes:
            # Open the box and add its keys to the queue
            opened_boxes.add(key)
            keys_to_explore.extend(boxes[key])

    # Check if all boxes have been opened
    return len(opened_boxes) == n
