arr = [13,46,24,52,20,9]
n = len(arr)
mini = arr[0]

for i in range(n):
    for j in range(i,n):
        if arr[j]<mini:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            mini = arr[i+1]
    
print(arr)