1. Joining SparseMatrix objects with hstack gives a matrix with the sum of the columns when all have zero rows: zeros(0,0), zeros(0,1), zeros(0,2), zeros(0,3) give shape (0, 6).
2. The same holds for vstack of matrices with zero columns: zeros(0,0), zeros(1,0), zeros(2,0), zeros(3,0) give shape (6, 0).
3. Matrices with one row (or one column) still stack to shape (1, 6) (or (6, 1)).
4. Joining an empty matrix with a non empty matrix keeps the entries of the non empty matrix.
