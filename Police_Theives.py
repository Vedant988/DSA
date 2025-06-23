class Solution:
    def catchThieves(self, arr, k):
        police = []
        thieves = []
        count = 0
    
        for i in range(len(arr)):
            if arr[i].upper()=='P':
                police.append(i)
            elif arr[i].upper()=='T':
                thieves.append(i)
    
        i=j=0
    
        while i<len(police) and j<len(thieves):
            if abs(police[i]-thieves[j])<=k:
                count+=1
                i+=1
                j+=1
            elif police[i]<thieves[j]:
                i+=1
            else:
                j+=1
    
        return count