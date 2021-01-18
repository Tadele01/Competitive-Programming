'''
    given integer ---> start from 1 until we reach the given integer we increment * by one and decrement space by 1

    
'''

def bethel_triangle(n):
    index = 1
    for i in range(n-1, -1, -1):
        space = ' ' * i
        star = '*' * index
        concat = space + star
        print(concat)
        index +=1

bethel_triangle(5)
        