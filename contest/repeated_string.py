def repeatedString(s, n):
    if s == 'a':
        return n
    if n < len(s):
        dis = len(s) - n
        s = s[:dis+1]
        count = 0
        for elt in s:
            if elt == 'a':
                count +=1
        return count
    length = len(s)
    div = n // length
    mod = n % length
    occurence = []
    for i in range(length):
        if s[i] == 'a':
            occurence.append(i+1)
    in_s_occurence = len(occurence)
    all_ = div * in_s_occurence
    count = 0
    for i in range(mod):
        if s[i] == 'a':
            count +=1
    all_ = all_ + count
    return all_
    