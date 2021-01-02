def repeatedString(s, n):
    length = len(s)
    div = n // length
    mod = n % length
    all_a = 0
    for i in range(length):
        if s[i] == 'a':
            all_a +=1
    all_a = div * all_a
    for i in range(mod):
        if s[i] == 'a':
            all_a +=1
    return all_a
    