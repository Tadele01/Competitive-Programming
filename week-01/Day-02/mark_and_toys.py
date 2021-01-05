def maximumToys(prices, k):
    '''
        the thought i have right now is can we remove first all the toys
        mark can't buy which is the toy with price greater than marks budget
        
        why do we want to remove all these values ?
           for optimizing our sorting a little bit for practice purpose 
    '''
    
    '''mark_range = []
    for elt in prices:
        if k >= elt:
            mark_range.append(elt)
    #now lets sort this array using counting sort my max element is k
    #since price can not be negative we don't care about negative value and make our
    #min price is 1
    counter = [0] * (k+1)
    for price in mark_range:
        counter[price] +=1
    sorted_prices = []
    for i in range(len(counter)):
        for j in range(counter[i]):
            sorted_prices.append(i)
    
    max_buy = 0
    index = 0
    count = 0
    while len(sorted_prices) > index:
        max_buy += sorted_prices[index]
        if max_buy <=k:
            count +=1
        if max_buy > k:
            return count
        index +=1
    return count'''
    sorted_prices = sorted(prices)
    max_buy = 0
    index = 0
    count = 0
    while len(sorted_prices) > index:
        max_buy += sorted_prices[index]
        if max_buy <=k:
            count +=1
        if max_buy > k:
            return count
        index +=1
    return count