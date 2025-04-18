import numpy as np
import scipy as sp
import time

def logpdf(X, m, C):
    N, D = X.shape

    C_obr = np.linalg.inv(C)
    logdet = np.linalg.slogdet(C)[1]

    quad_form = np.sum(((X - m) @ C_obr) * (X - m), axis=1)
    result = -0.5 * (D * np.log(2 * np.pi) + logdet + quad_form)
    return result


N, D = 1000, 3
m = np.zeros(D)
C = np.array([[2, 0.3, 0.5],[0.3,1,0.2],[0.5,0.2,1]])
X = np.random.multivariate_normal(m, C, N)

start1 = time.time()
my_logpdf = logpdf(X, m, C)
print("Time my log = ", time.time() - start1)

start2 = time.time()
sp_logpdf = sp.stats.multivariate_normal(m, C).logpdf(X)
print("Time scipy = ", time.time() - start2)
print(f"My results: {my_logpdf}")
print(f"Scipy results: {sp_logpdf}")

max_dev = 0
for i in range(min(my_logpdf.size, sp_logpdf.size)):
    max_dev = max(max_dev, np.abs(my_logpdf[i] - sp_logpdf[i]))
print("Max deviation = ", max_dev)

