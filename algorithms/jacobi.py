import scipy
import scipy.linalg
import numpy as np

import yaml
import logging
import logging.config

with open('utils/logging.yaml') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
logger.debug('This is a debug')

from utils.decorators import _timerStatistics


class Jacobi:
    """	
    Description
        A class implementing the jacobi method
        
    Attributes
        A -> list[list(float)]: Matrix
        b -> list(float): Vector
        x -> list(float): Solution vector
        _maxiter -> int: Maximum allowable iterations
        
    Methods
        jacobiMethodSlow: Computes system of equation using
            pythonic style jacobi method.
    """
    
    def __init__(self, A, b, x, maxiter = 1000) -> None:
        self.A = A
        self.b = b
        self.x = x
        self.maxiter = maxiter
        
        self.Anp = np.array(A, ndmin=2, dtype=np.float64)
        self.bnp = np.array(b, ndmin=2, dtype=np.float64).T
        self.xnp = np.array(x, ndmin=2, dtype=np.float64).T
        
    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}('
            f'{self.A!r}, {self.b!r})')
    
    def __str__(self) -> str:
        InputMatrix = 'Input matrix: \n'+'\n'.join(
            ['  '.join(['{:4}'.format(item) for item in row]) 
            for row in self.A]
        )
        Vector = '\n \n Vector: \n'+'\n'.join(
            ['{:4}'.format(item) for item in self.b]
        )
        return InputMatrix + Vector
    
    @_timerStatistics
    def jacobiLoop(self):
        """	
        Description
           	Computes system of equation using
            pythonic style jacobi method
        Returns
                list(float): Solution vector
        """
        iter = 0
        criteria = False
        x = self.x.copy()
        
        while iter < self._maxiter:
            iter+=1
            xOld = x.copy()
            for i in range(len(x)):
                outerSum = 0
                for j in range(len(x)):
                    if j != i:
                        outerSum += self.A[i][j] * x[j]
                x[i] = 1/self.A[i][i] * (self.b[i] - outerSum)
                
            criteria = all([abs(n - m) <= 1e-10 for n, m in zip(x, xOld)])
            if criteria:
                break
        return x
    
    @_timerStatistics
    def jacobiVectorised(self):
        iter = 0
        criteria = False
        xnp = self.xnp
        
        U = np.triu(self.Anp, k=1)
        L = np.tril(self.Anp, k=-1)
        D = np.diag(np.diag(self.Anp))
        
        Dinv = scipy.linalg.inv(D)
        LU = L + U
        
        while iter < self._maxiter:
            iter+=1
            xOld = xnp.copy()
            xnp = Dinv@(self.bnp - LU@xnp)
            criteria = np.allclose(xnp, xOld, rtol=0., atol=1e-10)
            if criteria:
                break
        return xnp
    
    @property
    def maxiter(self):
        """Doc string in getter: maxiter property"""
        logger.info(f"Accessing maxiter, value: {self._maxiter}")
        return self._maxiter
    
    @maxiter.setter
    def maxiter(self, value):
        if value <= 0:
            raise ValueError("Iterations must be above zero")
        if not isinstance(value, int):
            raise TypeError("MAXITER must be an integer")
        logger.info(f"Mutating maxiter to: {value}")
        self._maxiter = value
