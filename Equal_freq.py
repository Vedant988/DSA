class Solution:
    def sameFreq(self, s: str) -> bool:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        lst = list(freq.values())
        
        if len(set(lst)) == 1:
            return True
        for i in range(len(lst)):
            temp = lst.copy()
            temp[i] -= 1
            if temp[i] == 0:
                temp.pop(i)
            if len(set(temp)) == 1:
                return True
        return False