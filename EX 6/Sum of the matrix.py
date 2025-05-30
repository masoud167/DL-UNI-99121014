import numpy as np
import time

# Create a 1000x1000 matrix with random numbers
matrix = np.random.rand(1000, 1000)

# Measure time for row-wise sum
start_row = time.time()
row_sum = np.sum(matrix, axis=1)
end_row = time.time()
row_time = end_row - start_row

# Measure time for column-wise sum
start_col = time.time()
col_sum = np.sum(matrix, axis=0)
end_col = time.time()
col_time = end_col - start_col

# Print the results
print(f"Row sum time: {row_time:.6f} seconds")
print(f"Column sum time: {col_time:.6f} seconds")
