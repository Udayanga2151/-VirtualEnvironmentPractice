import numpy as np
import time

size = 1000000

start_time = time.time()
py_list = list(range(size))
square_list =[]

for x in py_list:
    square_list.append(x*x)
end_time = time.time()

duration = end_time-start_time
print(f"Python List time : {duration:.10f} seconds")

start_time = time.time()
np_arr = np.arange(size)
sq_arr = np_arr*np_arr
end_time = time.time()

duration = end_time - start_time
print(f"Python numpy time : {duration:.10f} seconds")
