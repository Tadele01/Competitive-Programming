def remove_duplicates(S):
    arr = []
    for letter in S:
        if arr:
            top = arr.pop()
            if top == letter:
                continue
            else:
                arr.append(top)
                arr.append(letter)
        else:
            arr.append(letter)
    new_string = ''.join(arr)
    return new_string