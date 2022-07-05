import time
from reader import feed

def approach1():
    """code works, not pythonic"""
    tic = time.perf_counter()
    #code here
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.7f} seconds")

def approach2():
    """code works, and pythonic"""
    tic = time.perf_counter()
    #code here
    toc = time.perf_counter()
    print(f"Downloaded the tutorial in {toc - tic:0.7f} seconds")


if __name__ == "__main__":
    main()