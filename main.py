from algorithms.jacobi import Jacobi

A = [
    [10., -1., 2., 0.],
    [-1., 11., -1., 3.],
    [2., -1., 10., -1.],
    [0.0, 3., -1., 8.]
]

b = [6., 25., -11., 15.]

x = [0, 0, 0, 0]

if __name__ == "__main__":
    algorithm = Jacobi(A, b, x)
    solution = algorithm.jacobiMethodSlow()