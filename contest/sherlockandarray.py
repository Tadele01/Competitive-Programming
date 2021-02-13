from collections import deque
def balancedSums(arr):
    '''
        using two pointers technique
            initially start with pop two elements one from the left and one from the right
            compare them do poping elements from the side where we have a low value
            while doing that keep left sum and right sum and when we encounter a case where the left sum and 
            the right sum are equal and only there is 1 element  in the array then we can return True otherwise return
            False
            
            
            l = 2
            r = 2
    '''
    d = deque(arr)
    left_sum, right_sum = 0, 0
    while d and len(d) != 1 :
        if left_sum == right_sum:
            left_sum += d.popleft()
            right_sum += d.pop()
        elif left_sum > right_sum:
            right_sum += d.pop()
        elif right_sum > left_sum:
            left_sum += d.popleft()
    if left_sum == right_sum or left_sum == 0 or right_sum == 0:
        return 'YES'
    return 'NO'
