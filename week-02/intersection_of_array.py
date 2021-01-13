def intersection(arr1, arr2):
    inter_section = []
    for elt in arr1:
        if elt in arr2 and elt not in inter_section:
            inter_section.append(elt)
    return inter_section
