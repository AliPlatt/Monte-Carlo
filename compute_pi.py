import numpy as np
import time 

'''pseudocode:
    1. generate random points inside a 1x1 square
    2. count how many points fall inside the unit circle
    3. calculate the ratio of points inside the circle to total points
    4. multiply the ratio by 4 to estimate the value of pi
'''
num_samples = int(input("Input number of samples:"))

x = np.random.uniform(0, 1, num_samples)
y = np.random.uniform(0, 1, num_samples)

def if_loop(x, y, num_samples):
    inside_circle = 0 
    for i in range(num_samples):
        if x[i]**2 + y[i]**2 <= 1:
            inside_circle += 1
    return inside_circle

def vectorised(x, y):
    return np.sum(x**2 + y**2 <= 1)

start = time.perf_counter()

#inside_circle = if_loop(x, y, num_samples)
inside_circle = vectorised(x, y)

elapsed = time.perf_counter() - start

pi_estimate = (inside_circle / num_samples) * 4
print(f"Estimated value of pi: {pi_estimate}")
print(f"Time taken: {elapsed:.4f} s")




