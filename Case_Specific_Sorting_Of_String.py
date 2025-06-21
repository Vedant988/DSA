class Solution:
    def caseSort(self,s):
        arr = []
        up = []
        low = []
        for i in s:
            if i.isupper():
                arr.append(1)
                up.append(i)
            else:
                arr.append(0)
                low.append(i)
        
        up = sorted(up)
        low = sorted(low)
        
        result = []
        up_idx = 0
        low_idx = 0
        
        for n in arr:
            if n == 1:
                result.append(up[up_idx])
                up_idx += 1
            else:
                result.append(low[low_idx])
                low_idx += 1
        final = "".join(result)
        return final