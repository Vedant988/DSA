def longest_2_distinct_custom(arr):
    if not arr:
        return 0

    orep = []
    prev = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] == prev:
            count += 1
        else:
            orep.append((prev, count))
            prev = arr[i]
            count = 1
    orep.append((prev, count))  

    max_len = 0

    for i in range(len(orep)):
        max_len = max(max_len, orep[i][1])

        if i + 1 < len(orep):
            val1, len1 = orep[i]
            val2, len2 = orep[i + 1]
            if len({val1, val2})<=2:
                max_len = max(max_len, len1 + len2)

        if i+2<len(orep):
            val1, len1 = orep[i]
            val2, len2 = orep[i + 1]
            val3, len3 = orep[i + 2]
            if len({val1, val2, val3}) <= 2:
                max_len = max(max_len, len1 + len2 + len3)

    return max_len

arr = [12,13,12,13,14,16,9,6,19,10,12,20,19,7]
ans = longest_2_distinct_custom(arr)
print(ans)
