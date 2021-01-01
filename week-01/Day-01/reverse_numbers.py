#reverse integers

def reverse(x: int) -> int:
    y = list(str(x))
    negative = None
    if y[0] == '-':
        negative = True
        y.pop(0)
    y.reverse()
    y = ''.join(y)
    y = int(y)
    if y > (-2147483648) and y <(2147483647):
        if negative:
            return -1 * y
        return y
    return 0