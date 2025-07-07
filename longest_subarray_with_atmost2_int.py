
def totalElements( arr):
    l,r,maxlen=0,0,-1
    map={}
    while(r<len(arr)):
        if arr[r] in map:
            map[arr[r]]+=1
        else:
            map[arr[r]]=1
        while(len(map))>2:
            map[arr[l]]-=1
            if map[arr[l]]==0:
                del map[arr[l]]
            l+=1
        if len(map)<3:
            maxlen = max(maxlen,r-l+1)
        r+=1
    return maxlen

arr = [7,14,17,18,5,9,20,14,19,7,16,11,7,11,10,10,15,6,14]     
ans = totalElements(arr)
print(ans)