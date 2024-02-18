def two_sum(arr, target):
    res = {}
    for x, num in enumerate(arr):
        y = target - num
        if y in res:
            return [res[y], x]
        res[num] = x

arr = [2,7,11,15]
target = 9

res = two_sum(arr, target)
print(res)
