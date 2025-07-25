
def custom_serach(s,substr):
    track = {}
    for i in range(len(substr)):
        if substr[i] in track:
            track[substr[i]]=i
        else:
            track[substr[i]]=0
    print(track)
    return 1








s = "abcdabcababb"
tofind="abbcabcaab"
ans = custom_serach(s,tofind)