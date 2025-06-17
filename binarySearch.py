# SORTED increasing array
def binary_search(arr,target):
    left,right=0,len(arr)
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,2,4,5,6,77,102,233,345,553,554,555,556,559]
num = binary_search(arr,556)
print(num)