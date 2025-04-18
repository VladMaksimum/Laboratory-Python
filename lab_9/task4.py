import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0]) 

x= np.array([x[i] for i in range(1,x.size) if x[i-1]==0])
print(x.max())