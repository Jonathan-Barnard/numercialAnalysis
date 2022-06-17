import logging

logging.basicConfig(
    format="%(asctime)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S"
)


A = [
    [10., -1., 2., 0.],
    [-1., 11., -1., 3.],
    [2., -1., 10., -1.],
    [0.0, 3., -1., 8.]
]
# initialize the RHS vector
b = [6., 25., -11., 15.]

x = [0, 0, 0, 0]


class Jacobi:
    """
    A class implementing the jacobi method
    
    Additionally this displays a managed attribute self.maxiter.
    Managed attributes can be used for:
        - Data validation from user or other sources
        - Read only, read-write or write only attrs
        - Computed attributes (lazy compute of value)
        - Auto formatting
        
    They perform better than asserts as you can turn asserts off in
    python optimised mode by setting __debug__ to false. During this
    asserts are ignored and code can perform not as expected.
    Asserts are still useful for:
        - Documenting: assert 2==2, "2 must equal 2"
        - Debugging: assert 2==2
        - Testing: def test_two: assert 2==2
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
    
    def jacobiMethodSlow(self):
        assert self.MAXITER >= 0, "Iterations must be above zero"
        pass
    
    @property
    def maxiter(self):
        """Doc string in getter: maxiter property"""
        logging.info(f"Accessing maxiter, value: {self._maxiter}")
        return self._maxiter
    
    @maxiter.setter
    def maxiter(self, value):
        if value <= 0:
            raise ValueError("Iterations must be above zero")
        if not isinstance(value, int):
            raise TypeError("MAXITER must be an integer")
        logging.info(f"Mutating maxter: {value}")
        self._maxiter = value
    

algorithm = Jacobi(A, b, x, 10)
print(__debug__)
algorithm.maxiter = 5
algorithm.maxiter