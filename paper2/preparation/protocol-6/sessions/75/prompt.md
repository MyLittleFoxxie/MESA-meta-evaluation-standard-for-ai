The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
improve singularity handling in `inequalities.py`
While `_solve_inequality` eliminates singularities from the solution, the higher level `reduce_inequalities` can eliminate singularities before that function gets solved:

<img width="412" height="157" alt="Image" src="https://github.com/user-attachments/assets/5ddeb305-73aa-4ee9-956b-903a0cc81741" />
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
