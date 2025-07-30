def subarray_sumk(arr,k):
    left = 0
    combiner = 0
    max_len = 0
    for right in range(len(arr)):
        combiner += arr[right]
        while combiner>k and left<=right:
            combiner-=arr[left]
            left+=1
        if combiner == k:
            max_len = max(max_len, right - left + 1)
    return max_len
