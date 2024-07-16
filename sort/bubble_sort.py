from timer import timer

@timer
def bubble_sort(li):
    for x in range(len(li) - 1): # 1趟
        for y in range(len(li) - x - 1):
            if li[y] > li[y + 1]:
                li[y], li[y + 1] = li[y + 1], li[y]
    return li

def my_sort(li):
print()