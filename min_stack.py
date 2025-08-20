nums = [23,25,45,17,38,31,21,35,44]
stck =[]
stck.append([nums[0],nums[0]])
for i in nums[1:]:
    if i<stck[-1][1]:
        low=i
    else:
        low=stck[-1][1]
    stck.append([i,low])

def getmin():
    return stck[-1][1]