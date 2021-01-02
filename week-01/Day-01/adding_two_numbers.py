#inorder to add two numbers without using addition operator we can treat those numbers as strings and
#do primary school addition on a single digits

'''
    we go from right to left convert each char to int step by step since we use base 10 if the summation
    of two single digit number exceed 10 we store the first element and carry it to the next operation

        -> 255
          +244  

          for this what we're going to do is we start from 5+4(which is the right most element of the two numbers)
          which give us 9, it is less than 10 we continue 5+4, give us 9, continue 2+2 , 4
          then our answer will be 499



'''
def to_string(l):
    return list(str(l))

def reverse(l):
    rev = []
    for i in range(len(l)-1, -1, -1):
        rev.append(str(l[i]))
    
    return ''.join(rev)
def add_two_numbers(num1, num2):
    num1_str = to_string(num1)
    num2_str = to_string(num2)
    len1 = len(num1_str)
    len2 = len(num2_str)
    if len1 < len2:
        num1_str, num2_str = num2_str, num1_str
    len1, len2 = len2, len1
    summation = []
    carrier = 0
    while len(num2_str) !=0:
        i = len(num1_str) - 1
        j = len(num2_str) - 1
        add = int(num1_str.pop(i)) + int(num2_str.pop(j)) + carrier
        if add >= 10 :
            add_str = to_string(add)
            summation.append(add_str[1])
            carrier = int(add_str[0])
        else:
            carrier = 0
            summation.append(add)
    if carrier != 0 or len(num1_str) != 0:
        if len(num1_str) !=0:
            for i in range(len(num1_str)-1, -1, -1):
                v = add_two_numbers(int(num1_str[i]), carrier)
                if len(v) ==2:
                    summation.append(v[1])
                    carrier = int(v[0])
                else:
                    summation.append(v)
                num1_str.pop()
            if carrier != 0:
                summation.append(carrier)
        else:
            summation.append(carrier)
    summation = reverse(summation)
    return summation

print(add_two_numbers(1111111111111111111111111111, 991111111111111111111111111111111111111119))


