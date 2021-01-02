#reverse integers

def reverse(x: int) -> int:
    num = ''
    negative = False
    if x < 0:
        negative = True
        x = -1*x
    while x != 0:
        rem = x % 10
        x = x // 10
        num += str(rem)
    num = int(num)
    if num > (-2147483648) and num <(2147483647):
        if negative:
            return -1 * num
        return num
    return 0
print(reverse(-2147483648))