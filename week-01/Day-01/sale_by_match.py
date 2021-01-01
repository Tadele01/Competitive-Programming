def sale_by_match(l, length):
    hash_map = dict()
    pair = 0
    for i in range(length):
        if l[i] in hash_map:
            v = hash_map[l[i]]
            pair +=1
            hash_map[l[i]] = 0
        else:
            hash_map[l[i]] = 1
    accumlator = 0
    for key in hash_map:
        if hash_map[key] > 1:
            accumlator += hash_map[key] // 2
    return accumlator
l = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
length = 10
print(sale_by_match(l, length))