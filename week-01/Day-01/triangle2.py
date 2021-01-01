#equilateral triangle drawer
def triangle_2(n):
    #n should be an odd number to get perfect triangle otherwise left and right can not be balanced
    #if the inputted number is even we get the max odd number which is less than the input number's triangle
    counter = n//2
    for i in range(n+1):
        if i % 2 == 1:
            print(' '*counter , '*'*i)
            counter -=1
