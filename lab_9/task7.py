import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

uniq = set()
print(iris.shape)
cnt=0

for i in range(iris.shape[0]):
    if iris[i][4] not in uniq:
        cnt+=1
    uniq.add(iris[i][4])
    

print("Uniq spieces: ", uniq)
print("Quantity: ", cnt)

