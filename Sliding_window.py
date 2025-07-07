def longestKSubstr(s, k):
    map = {}
    l,r = 0,0
    maxlen=0
    while r<len(s):
        if s[r] in map:
            map[s[r]]+=1
        else:
            map[s[r]]=1
        print(map)
        while(len(map))>k:
            print(s[l])
            map[s[l]]-=1
            if map[s[l]]==0:
                del map[s[l]]
            l+=1
        if len(list(map.values()))<=k:
            maxlen = max(maxlen,r-l+1)
        r+=1
        
    print(map)
    print()
    return maxlen

s = "aabasde"
k = 3
ans = longestKSubstr(s,k)
print("ans:",ans)
                
            