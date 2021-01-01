#counting valley 

def counting_valley(steps, l):
    sea_level = 0
    count = 0
    for i in range(l):
        if steps[i] == 'U':
            sea_level += 1
        elif steps[i] == 'D':
            sea_level -= 1
        if steps[i] == 'U' and sea_level == 0:
            count +=1
    
    return count
print(counting_valley('DDUUDDUDUUUD', 12))