The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Division by zero error in reshape
sympy.reshape((1,),how=()) fails with division by zero error, after it sums how, and divides the length of the main argument by it, and only after that checks if it is less than 0 and raises a ValueError
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
