import time

def approach1():
    """code works, not pythonic"""
    sum = 0
    # start time
    tic = time.time()
    # piece of code
    for i in range(100000):
        sum+=i
    # end time
    toc = time.time()
    print(f"For loop took {toc - tic:0.7f} seconds")

def approach2():
    """code works, and pythonic"""
    sum = 0
    # start time
    tic = time.perf_counter()
    # piece of code
    for i in range(100000):
        sum+=i
    # end time
    toc = time.perf_counter()
    print(f"For loop took {toc - tic:0.7f} seconds with perf_counter")


if __name__ == "__main__":
    # approach1()
    approach2()   