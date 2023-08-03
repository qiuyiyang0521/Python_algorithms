
def bubble_sort(li):
    for x in range(len(li) - 1): # 1趟
        for y in range(len(li) - x - 1):
            if li[y] > li[y + 1]:
                li[y], li[y + 1] = li[y + 1], li[y]
    return li


li = [5.9,8,6,3,2,4,8,6,5]
li = bubble_sort(li)
print(li)
