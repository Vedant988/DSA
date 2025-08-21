class Solution:
    def countBalanced(self, arr):
        vowels = {'a', 'e', 'i', 'o', 'u'} 

        def get_balance_value(s):
            balance=0
            for char in s:
                if char in vowels:
                    balance+=1
                else:
                    balance-=1
            return balance

        balance_values=[]
        for s in arr:
            balance_values.append(get_balance_value(s))
            
        prefix_sum_counts={0:1}
        current_sum=0
        count=0

        for value in balance_values:
            current_sum += value
            if current_sum in prefix_sum_counts:
                count += prefix_sum_counts[current_sum]
            prefix_sum_counts[current_sum] = prefix_sum_counts.get(current_sum,0)+1
            
        return count