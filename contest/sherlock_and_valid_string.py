from collections import Counter
def isValid(s):
    counter = Counter(s)
    values = Counter(counter.values())
    if len(values.keys())==1:
        return "YES"
    elif len(values.values())==2:
        key1, key2 = values.keys()
        if values[key1]==1 and (key1-1==key2 or key1-1==0):
            return "YES"
        elif values[key2]==1 and (key2-1==key1 or key2-1==0):
            return "YES"
        else:
            return "NO"

    else:
        return "NO"