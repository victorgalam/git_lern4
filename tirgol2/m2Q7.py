def what(arr, num):
    c = 0
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] >= num:
            right -= 1

        else:
            c+=(right - left)
            left+=1
        return c

arr = [1,3, 6, 11, 18, 21, 27, 35]
