# 向下调整函数
def sift(li, head, tail):
    """
    这个函数实现了堆的向下调整功能
    :param li: 列表
    :param head: 堆的根节点位置（即最上面的节点）
    :param tail: 堆的最后一个元素位置
    :return:
    """

    # li = li

    # i和j分别为节点和它的叶子节点，i其实就是有空位、待填充的一个节点
    # 此时i是最“上”面的节点
    i = head
    # (i * 2 + 1)为左子节点，(i * 2 + 2)为右子节点
    j = i * 2 + 1
    # 临时变量temp储存需要向下调整的节点
    temp = li[head]
    # 循环结束条件：当i为叶子节点时，没办法再次向下调整了，就结束循环，即j>tail，循环条件为j<=tail
    # 大白话：只要j有数可以替代i，循环就继续
    while j <= tail:
        # 先要比较两个子节点的大小，再决定哪个节点和父节点替换
        # 如果存在右子节点并且右子节点大于左子节点
        if j + 1 <= tail and li[j + 1] > li[j]:
            # j就指向右子节点
            j += 1
        # 如果子节点比temp大，就用大的子节点替换父节点
        if li[j] > temp:
            # 用大的子节点填充到空的父节点上
            li[i] = li[j]
            # 此时这j节点空出，待填补，成为新的i
            # 更新i和j
            i = j
            # 此时j为i的左子节点
            j = i * 2 + 1
        # 如果temp适合填补到i的空缺，即temp>j，那么这次向下调整就可以结束了
        else:
            # 将temp放入i
            li[i] = temp
            # 退出
            break
    # 这种情况就是temp太小了，也就是堆顶需要调整的那个数太小了，只能放到最后一级的叶子节点
    else:
        # 此时的i是一个空缺的叶子节点
        li[i] = temp


def heap_sort(li):
    """
    根排序主函数
    :param li: 列表
    :return:
    """

    li = li.copy()

    # 开始建堆
    # 获取最后一个叶子节点
    length = len(li)
    last = length - 1
    # 获取最后一个叶子节点的父节点
    n = (last - 1) // 2
    # 开始整理一个个“小堆”
    for i in range(n, -1, -1):
        # i表示当前整理部分的堆的根节点
        # 因一些“不可抗因素”，high就一直设为整个堆的最后一个元素，反正high也没有什么实际作用（实际上high是为了判断i下还有没有子节点，将high设为最后一个元素也可以达到相同的效果）
        sift(li, i, last)
    # 建堆完成
    print("Sorted list:", li)

    for i in range(length - 1, -1, -1):
        # i指向堆的最后一个元素
        # 堆的根节点和最后一个元素交换
        li[1], li[i] = li[i], li[1]


if __name__ == '__main__':
    li = [i for i in range(100)]
    from random import shuffle

    shuffle(li)
    print(li)
    heap_sort(li)
    print("Original list:", li)
