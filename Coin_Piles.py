from bisect import bisect_right
from itertools import accumulate

class Solution:
    def minimumCoins(self, arr, k):
        arr.sort()
        n = len(arr)

        prefix=list(accumulate(arr))
        min_cost=float('inf')

        for i in range(n):
            base=arr[i]
            upper=base+k

            removal_cost=prefix[i-1] if i > 0 else 0
            upper_idx = bisect_right(arr,upper)

            if upper_idx<n:
                reduce_sum = prefix[n-1] - prefix[upper_idx-1]
                reduce_cost = reduce_sum-(n-upper_idx)*upper
            else:
                reduce_cost = 0

            total_cost = removal_cost+reduce_cost
            min_cost = min(min_cost,total_cost)
        return min_cost
