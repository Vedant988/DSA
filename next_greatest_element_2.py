arri = [1,4,3,2,6,9,4,8,2]
n = len(arri)
nge = [-1 for j in range(n)]
nge2 = [-1 for j in range(n)]
print("program started")
stk = []
for i in range(n-1,-1,-1):
    while stk and arri[i]>=stk[-1]:
        stk.pop()
    if stk:
        nge[i]=stk[-1]
    stk.append(arri[i])

stk = []
for i in range(n-1,-1,-1):
    while stk and nge[i]>=stk[-1]:
        stk.pop()
    if stk:
        nge2[i]=stk[-1]
    stk.append(nge[i]) 
print("nge:",nge)
print("nge2:",nge2)

    
