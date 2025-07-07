def countAtMostK(arr, k):
    l,r,count=0,0,0
    map ={}
    while(r<len(arr)):
        if arr[r] in map:
            map[arr[r]]+=1
        else:
            map[arr[r]]=1
            
        while(len(map)>k):
            map[arr[l]]-=1
            if map[arr[l]]==0:
                del map[arr[l]]
            l+=1
        count +=1
        r+=1
    return count
arr = [1,2,2,3]
k = 2
ans = countAtMostK(arr,k)
print(ans)