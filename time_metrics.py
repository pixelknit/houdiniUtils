import time
import os
from memory_profiler import profile

def timing(f):
    def wrap(*args, **kwargs):
        start_time = time.monotonic()
        ret = f(*args, **kwargs)
        end_time = time.monotonic()
        print("{:s} funciont took {:.3f} ms".format(f.__name__, (end_time - start_time) * 1000.0))

        return ret
    return wrap

@profile
@timing
def test():
    for i in range(1000000):
        print(i**2)


if __name__ == "__main__":
    test()
