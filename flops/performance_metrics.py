import time
import numpy as np

N = 2096

if __name__ == "__main__":
    A = np.random.randn(N,N).astype(np.int8)
    B = np.random.randn(N,N).astype(np.int8)

    flop = N*N*2*N

    print(f"{flop / 1e9:.2f} GFLOP")

    start_time = time.monotonic()

    C = A @ B

    end_time = time.monotonic()

    s = end_time - start_time

    print(f"{flop/s * 1e-9:.2f} GFLOPS")
    print(f"{flop/s * 1e-12:.2f} TFLOPS")
