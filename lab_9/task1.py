import numpy as np

with open("lab_9/numbers.txt") as file:
    matrix = np.array([i.split(',') for i in file.readlines()], dtype=int)
    print("sum of elements = ", matrix.sum())
    print("min element = ", matrix.min())
    print("max element = ", matrix.max())