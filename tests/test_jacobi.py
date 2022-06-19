import pytest

from algorithms.jacobi import Jacobi 


A = [[0, 0], [0, 0]]
b = [0, 0]
x = [0, 0]


def testGetsMaxiter():
    algorithm = Jacobi(A, b, x, maxiter=100)
    assert algorithm.maxiter == 100


def testSetsMaxiter():
    algorithm = Jacobi(A, b, x, maxiter=100)
    algorithm.maxiter = 50
    assert algorithm.maxiter == 50


def testMaxiterTypeError():
    with pytest.raises(TypeError):
        Jacobi(A, b, x, maxiter="hi")
        Jacobi(A, b, x, maxiter=1.)
        Jacobi(A, b, x, maxiter=True)


def testMaxiterValueError():
    with pytest.raises(ValueError):
        Jacobi(A, b, x, maxiter=0)
        Jacobi(A, b, x, maxiter=-1)
