def linear_search(li, value):
    for index, val in enumerate(li):
        if val == value:
            return index
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(li, 5))