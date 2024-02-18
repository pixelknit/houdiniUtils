def three_sum(arr, target):
    arr.sort()
    res = []

    for i in range(len(arr)-2):
        left = i +1
        right = len(arr) -1

        while left < right:
            current_sum = arr[i] + arr[left]+ arr[right]
            if current_sum == target:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1

            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1

    return res

nums = [3,7,1,2,8,4,5]
target= 20

res = three_sum(nums, target)
print(res)
