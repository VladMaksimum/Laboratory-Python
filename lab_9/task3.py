import numpy as np

rand_mass = np.random.normal(50, 100, 40).reshape(10,4)
print(rand_mass)
print("average = ", rand_mass.mean())
print("min = ", rand_mass.min())
print("max = ", rand_mass.max())
print("deviation = ", rand_mass.std())

five = np.array([rand_mass[i] for i in range(5)])
print(five)