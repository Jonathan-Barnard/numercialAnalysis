import numpy as np

from algorithms.jacobi import Jacobi
from algorithms.statistics import Statistics

#A = [
#    [10., -1., 2., 0.],
#    [-1., 11., -1., 3.],
#    [2., -1., 10., -1.],
#    [0.0, 3., -1., 8.]
#]

A = np.random.random((200, 200))

b = np.zeros(200) #[6., 25., -11., 15.]

x = np.zeros(200) #[0, 0, 0, 0]

if __name__ == "__main__":
    algorithm = Jacobi(A, b, x)
    statistics = Statistics(algorithm)
    print(statistics.performance())
