import time

def approach1():
    """works, but not preferred"""
    sum = 0
    # start time
    tic = time.time()
    # piece of code
    for i in range(100000):
        sum+=i
    # end time
    toc = time.time()
    print(f"Elapsed time: {toc - tic:0.7f} s.")

def approach2():
    """works, and  preferred"""
    sum = 0
    # start time
    tic = time.perf_counter()
    # piece of code
    for i in range(100000):
        sum+=i
    # end time
    toc = time.perf_counter()
    print(f"Elapsed time: {toc - tic:0.7f} s with perf_counter.")


if __name__ == "__main__":
    approach1()
    #approach2()   