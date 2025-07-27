def pge(arr):
    result = [-1]*len(arr)
    stack =[]
    print(result)
    for i in range(len(arr)):
        while(stack and arr[i]>=stack[-1]):
            stack.pop()
        if stack:
            result[i]=stack[-1]
        stack.append(arr[i])
    return result

arr = [13,2,5,7,8,,4,19,10,2]
ans = pge(arr)
print(ans)