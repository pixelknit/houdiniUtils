import math

def binSearch(arr: list, target: int) -> int:
    lo = 0
    hi = len(arr)

    while lo < hi:
        m = math.floor(lo + (hi-lo)/2)
        v = arr[m]

        if v == target:
            return m
        elif v > target:
            hi = m
        else:
            lo = m + 1

    return -1

