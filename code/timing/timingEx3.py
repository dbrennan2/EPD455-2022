import time
import argparse

def approach1():
    """works, but not preferred"""
    sum = 0    
    tic = time.time() # start watch
    for i in range(100000):
        sum+=i
    toc = time.time() # stop watch
    print(f"Elapsed time: {toc - tic:0.7f} s.")

def approach2():
    """works, and  preferred"""
    sum = 0
    tic = time.perf_counter() # start watch
    for i in range(100000):
        sum+=i    
    toc = time.perf_counter() # stop watch
    print(f"Elapsed time: {toc - tic:0.7f} s with perf_counter.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--choice', type = int, required = True, \
        help='Select 1 or 2 to experiment with two different types of timing.')
    args = parser.parse_args()
    if args.choice==1:
        approach1()
    elif args.choice==2:
        approach2()
    else:
        print("argument list no ok.")