import numpy as np

x = np.array([2, 2, 2, 3, 3, 3, 5])
x.sort()

nums = np.array([x[0]])
repeats = np.array([1])
index = 0

for i in range(1,x.size):
    if x[i] == x[i-1]:
        repeats[-1] +=1
    else:
        nums = np.append(nums, np.array([x[i]]))
        repeats = np.append(repeats, np.array([1]))
    print(nums, repeats)


print("nums: ", nums)
print("repeats: ", repeats)