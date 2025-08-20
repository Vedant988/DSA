str = "a+b*(c/d-e)"
operand=["+","-","*","/","^"]
stck=[]
res=[]
def priority(char):
    if (char=="+" or char=="-"):
        return 1
    elif (char=="*" or char=="/"):
        return 2
    elif char=="^":
        return 3
    elif char=="(":
        return 0

for i in str:
    if ((i>="A" and i<="Z") or (i>="a" and i<="z") or (i>="0" and i<="9")):
        res.append(i)
    elif i in operand:
        prio = priority(i)
        while stck and priority(stck[-1]) >= prio:
            res.append(stck.pop())
        stck.append(i)
    elif i=="(":
        stck.append(i)
    elif i == ")":
        while stck and stck[-1] != "(":
            res.append(stck.pop())
        if stck and stck[-1] == "(":
            stck.pop()
while stck:
    res.append(stck.pop())
print("".join(res))
