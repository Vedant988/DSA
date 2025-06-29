arr = [9,10,12,13,15,11]
n = len(arr)

def InsertionSort(arr):
    for i in range(n):
        j = i
        while(j>0 and arr[j-1]>arr[j]):
            temp = arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
            j-=1
    return arr
arr = InsertionSort(arr)
print(arr)
