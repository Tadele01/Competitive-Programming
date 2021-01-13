def intersection(arr1, arr2):
    '''inter_section = []
    for elt in arr1:
        if elt in arr2 and elt not in inter_section:
            inter_section.append(elt)
    return inter_section'''

    #alternative approch by using python built in set class

    set1 = set(arr1)
    set2 = set(arr2)
    inter_section = set1.intersection(set2)
    return inter_section
