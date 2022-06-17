### Notes on jacobi.py

Determines the solution of a system of linear equations as long as the matrix A is diagonally dominant.

#### Additional notes on class formation

A managed attribute named maxiter is used within this program. Managed attributes can be used for:

- Data validation from user or other sources.
  - A composition of a property inside another class can be used to follow DRY, for example when repetatively checking attributes are above zero
- Read only, read-write or write only attrs.
- Computed attributes (lazy compute of value).
- Auto formatting.
    
They perform better than asserts as you can turn asserts off in python optimised mode by setting `__debug__` to false. During this asserts are ignored and code can perform not as expected.

Asserts are still useful for:
- Documenting: assert 2==2, "2 must equal 2"
- Debugging: assert 2==2
- Testing: def test_two: assert 2==2