visited = set()


def canReach(arr, start):
    if start < 0 or start >= len(arr) or start in visited:
        return False

    if arr[start] == 0:
        return True

    visited.add(start)
    return canReach(arr, start + arr[start]) or canReach(arr, start - arr[start])