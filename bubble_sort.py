arr = [9,10,12,13,15,16]
n = len(arr)

def BubbleSort(arr):
    for i in range(n-1,0,-1):
        didswap=0
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                didswap+=1
                temp = arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
        if didswap==0:
            return arr
            
    return arr
arr = BubbleSort(arr)
print(arr)