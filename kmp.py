
def custom_serach(s,substr):
    track =[]
    st = substr[0]
    fd = len(substr)
    for i in range(s):
        if s[i] == st:
            track.append(i)
    for i in track:
        






s = "abcdabcababb"
tofind="abb"
ans = custom_serach(s,tofind)