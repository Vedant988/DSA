arr = [1,2,3,5,6,10,9,24]
arr = sorted(arr)

def longestmul(arr):
    midx=0
    mlen=0
    dp = [1]*len(arr)
    prev = [-1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if(arr[i]%arr[j]==0 and arr[j]+1>=arr[i]):
                dp[i]=dp[j]+1
                prev[i]=j
        if dp[i]>mlen:
            mlen=dp[i]
            midx=i
        result = []
    while midx != -1:
        result.append(arr[midx])
        midx = prev[midx]
    print(midx)
    print(mlen)
    return result[::-1]
    
    
arr = longestmul(arr)
print(arr)

                

