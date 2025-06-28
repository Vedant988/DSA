def largestSubset(arr):
    arr = sorted(arr)
    dp = [1]*len(arr)
    prev = [-1] *len(arr)
    
    mIdx = 0
    mLen = 0
    
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[i]%arr[j]==0 and dp[j]+1>=dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > mLen:
            mLen = dp[i]
            mIdx = i
    result = []
    while mIdx != -1:
        result.append(arr[mIdx])
        mIdx = prev[mIdx]
    return result[::-1]

arr = [1,2,5,7,8,16,32,14,10]       
res = largestSubset(arr)
print(res)