from random import shuffle
import time


def partition(data: list, left: int, right: int) -> int:
    # 选择第一个元素作为基准元素
    tmp = data[left]
    # 循环直到左指针和右指针相遇
    while left < right:
        # 从右往左，找到小于基准元素的值
        while data[right] > tmp and left < right:
            right -= 1
        # 将小于基准元素的值放到左指针位置
        data[left] = data[right]
        # 从左往右，找到大于基准元素的值
        while data[left] < tmp and left < right:
            left += 1
        # 将大于基准元素的值放到右指针位置
        data[right] = data[left]
    # 将基准元素放到最终位置
    data[left] = tmp
    # 返回基准元素的索引
    return left


def quick_sort(data: list, left: int, right: int) -> list:
    # print(f"{left}到{right}")

    # 如果左边索引小于右边索引，继续进行排序
    if left < right:
        # 选择基准元素并进行分区操作
        mid = partition(data, left, right)
        # 对基准元素左边的子数组进行递归排序
        quick_sort(data, left, mid - 1)
        # 对基准元素右边的子数组进行递归排序
        quick_sort(data, mid + 1, right)

    # print("排序完成")
    return data


if __name__ == '__main__':
    # 如果这个文件被直接执行，而不是被其他文件导入执行
    lst = list(range(10000))  # 创建一个包含1到9999的列表
    shuffle(lst)  # 随机打乱列表顺序
    time_start = time.time()  # 记录开始时间
    quick_sort(lst, 0, len(lst) - 1)  # 调用快速排序函数对列表进行排序
    time_stop = time.time()  # 记录结束时间
    print(time_stop - time_start)  # 打印排序所用时间
    print(lst)  # 打印排序后的列表

