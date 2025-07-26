class Solution:
    def nextLargerElement(self, arr):
        stack = []
        brr = arr + arr
        result = [-1]*len(brr)
        for i in range(len(brr)-1,-1,-1):
            while stack and stack[-1]<=brr[i]:
                stack.pop()
                
            if stack:
                result[i]=stack[-1]
            stack.append(brr[i])
        result = result[0:len(arr)]
        return result
    