from timer import timer


def heapify(li: list, start_index: int, end_index: int) -> list:
    """
    给指定范围的列表堆化（向下调整）
    :param li: 需要堆化的列表
    :param start_index: 堆化范围根节点的索引
    :param end_index: 堆化范围最后一个节点的索引
    :return: 范围内堆化后的列表
    """
    li = li.copy()
    index = start_index
    left = 2 * start_index + 1
    right = 2 * start_index + 2

    while left <= end_index:

        # 在left node和right node中选出largest
        if right <= end_index and li[right] >= li[left]:
            largest_index = right
        elif right <= end_index and li[left] > li[right]:
            largest_index = left
        else:  # 这种情况下，没有右子节点，只有左子节点
            largest_index = left

        if li[largest_index] > li[index]:
            li[index], li[largest_index] = li[largest_index], li[index]
            index = largest_index
            left = 2 * index + 1
            right = left + 1
        else:
            break

    return li


def build_heap(li: list) -> list:
    """
    构建堆
    :param li: 需要构建堆的列表:
    :return: 堆结构的列表
    """
    li = li.copy()
    last_parent_node_index = (len(li) - 2) // 2
    for index in range(last_parent_node_index, -1, -1):
        li = heapify(li, index, len(li) - 1)

    return li


def heap_sort(li: list) -> list:
    li = li.copy()
    li = build_heap(li)
    for i in range(len(li) - 1, 0, -1):
        li[0], li[i] = li[i], li[0]
        li = heapify(li, 0, i - 1)
    return li
