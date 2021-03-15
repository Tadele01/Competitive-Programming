def superDigit(n, k):
    str_ = str(n)
    if len(str_) == 1 and k == 1:
        return int(str_)
    
    int_ = [int(i) for i in str_]
    sum_ = sum(int_) * k
    return superDigit(sum_, 1)