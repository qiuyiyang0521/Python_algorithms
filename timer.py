from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        run_time = end_time - start_time
        print("运行时间为{}".format(run_time))

    return wrapper
