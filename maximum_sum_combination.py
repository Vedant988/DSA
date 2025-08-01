import heapq
class Solution:
    def topKSumPairs(self, a, b, k):
        a = sorted(a,reverse=True)
        b = sorted(b,reverse=True)
        max_heap = []
        n = len(a)
        visited = set()
        heapq.heappush(max_heap,(-(a[0]+b[0]),0,0))
        visited.add((0,0))
        res = []
        for i in range(k):
            cur_sum,i,j = heapq.heappop(max_heap)
            res.append(-cur_sum)
            if (i+1)<n and (i+1,j) not in visited:
                heapq.heappush(max_heap,(-(a[i+1] + b[j]), i+1, j))
                visited.add((i+1,j))
            if (j+1)<n and (i,j+1) not in visited:
                heapq.heappush(max_heap,(-(a[i] + b[j+1]), i, j+1))
                visited.add((i,j+1))
        return res