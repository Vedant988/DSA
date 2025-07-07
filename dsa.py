def maxSum(arr):
    maxi = -1
    n = len(arr)
    for i in range(n):
        if i + 1 >= n:
            break  
        min1, min2 = arr[i], arr[i + 1]

        if min2 < min1:
            min1, min2 = min2, min1
        maxi = max(maxi, min1 + min2)

        for r in range(i + 2, n):
            num = arr[r]
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            maxi = max(maxi, min1 + min2)

    return maxi

arr = [4, 3, 5, 1]
ans = maxSum(arr)
print(ans) 
