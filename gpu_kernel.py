from numba import cuda
import numpy as np
import math

# CUDA kernel
@cuda.jit
def matmul_kernel(A, B, C):
    # Define an array in the shared memory
    # The size and type of the arrays must be known at compile time
    sA = cuda.shared.array(shape=(TPB, TPB), dtype=np.float32)
    sB = cuda.shared.array(shape=(TPB, TPB), dtype=np.float32)

    x, y = cuda.grid(2)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    bpg = cuda.gridDim.x

    if x >= C.shape[0] and y >= C.shape[1]:
        return

    # Each thread computes one element in the result matrix.
    tmp = 0.
    for i in range(bpg):
        # Preload data into shared memory
        sA[ty, tx] = A[y, tx + i * TPB]
        sB[ty, tx] = B[ty + i * TPB, x]

        # Wait until all threads finish preloading
        cuda.syncthreads()

        for j in range(TPB):
            tmp += sA[ty, j] * sB[j, tx]

        # Wait until all threads finish computing
        cuda.syncthreads()

    C[y, x] = tmp

# Matrix dimensions
N = 1024
TPB = 32

# Host code
A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)
C = np.zeros((N, N), dtype=np.float32)

# Configure the blocks
threadsperblock = (TPB, TPB)
blockspergrid_x = math.ceil(A.shape[0] / threadsperblock[0])
blockspergrid_y = math.ceil(B.shape[1] / threadsperblock[1])
blockspergrid = (blockspergrid_x, blockspergrid_y)

# Start the kernel
matmul_kernel[blockspergrid, threadsperblock](A, B, C)

print(C)

