class Solution:
    def maxSum(self, arr):
        maxi = -1
        n = len(arr)
        for i in range(n-1):
            min1,min2 = arr[i],arr[i+1]
            maxi = max(maxi,min1+min2)
        return maxi