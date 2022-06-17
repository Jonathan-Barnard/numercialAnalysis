from utils.decorators import _timer
from utils.logging import logger

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
        self._maxiter = maxiter
        
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
    
    @_timer
    def jacobiMethodSlow(self):
        """	
        Description
           	Computes system of equation using
            pythonic style jacobi method
        Returns
                list(float): Solution vector
        """
        iter = 0
        
        while iter < self._maxiter:
            xOld = self.x.copy()
            for i in range(len(self.x)):
                outerSum = 0
                for j in range(len(self.x)):
                    if j != i:
                        outerSum += self.A[i][j] * self.x[j]
                self.x[i] = 1/self.A[i][i] * (self.b[i] - outerSum)
                
            criteria = all([abs(n - m) <= 1e-10 for n, m in zip(self.x, xOld)])
            if criteria:
                break
            iter+=1
        return self.x
    
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
