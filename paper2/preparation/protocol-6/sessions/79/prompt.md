The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
integrate exp(x)/(x-1)
This should be a simple integral, but the integrator is clueless towards the correct u-sub.

```python
In [1]: integrate((exp(x)/(x-1)), x)
Out[1]:
⌠
⎮   x
⎮  ℯ
⎮ ───── dx
⎮ x - 1
⌡

In [2]: integrate((exp(x)/(x-1)).subs(x, y+1), y)
Out[2]: ℯ⋅Ei(y)

In [3]:
```
integrate x**2*sin(x**2)*cos(x)
SymPy:
```python
In [12]: integrate(x**2*sin(x**2)*cos(x), x)
Out[12]: 
⌠                     
⎮  2    ⎛ 2⎞          
⎮ x ⋅sin⎝x ⎠⋅cos(x) dx
⌡                     

In [13]: manualintegrate(x**2*sin(x**2)*cos(x), x)
Out[13]: 
                     ⌠                     ⌠                    
                     ⎮           ⎛ 2⎞      ⎮             ⎛ 2⎞   
              ⎛ 2⎞   ⎮ cos(x)⋅cos⎝x ⎠ dx   ⎮ x⋅sin(x)⋅cos⎝x ⎠ dx
  x⋅cos(x)⋅cos⎝x ⎠   ⌡                     ⌡                    
- ──────────────── + ─────────────────── - ─────────────────────
         2                    2                      2          
```

Wolfram Alpha:
<img width="1040" height="568" alt="Image" src="https://github.com/user-attachments/assets/8c3496f2-bb32-47b2-b4b2-3d7e484db72d" />
integral of `p(x)*fresnelc(q(x))` where p and q are polynomials
Sympy:

```python
In [8]: integrate(x*fresnelc(sqrt(2)*(2*x + 1)/(2*sqrt(pi))), x)
Out[8]: 
⌠                    
⎮    ⎛√2⋅x    √2 ⎞   
⎮ x⋅C⎜──── + ────⎟ dx
⎮    ⎝ √π    2⋅√π⎠   
⌡                    
```

Wolfram Alpha:

<img width="1040" height="317" alt="Image" src="https://github.com/user-attachments/assets/45f07a26-63d7-41b3-a9e9-14c362e0b500" />
integrate `sin(x**2+x)*cos(x)`
SymPy:

```python
In [3]: integrate(sin(x**2 + x)*cos(x), x)
Out[3]: 
⌠                      
⎮    ⎛ 2    ⎞          
⎮ sin⎝x  + x⎠⋅cos(x) dx
⌡                      

In [4]: manualintegrate(sin(x**2 + x)*cos(x), x)
Out[4]: 
⌠                      ⌠                         
⎮    ⎛ 2⎞    2         ⎮                  ⎛ 2⎞   
⎮ sin⎝x ⎠⋅cos (x) dx + ⎮ sin(x)⋅cos(x)⋅cos⎝x ⎠ dx
⌡                      ⌡                         
```

Wolfram Alpha:

<img width="1040" height="281" alt="Image" src="https://github.com/user-attachments/assets/20c81826-9065-4a5d-8537-fc97c1939a75" />
integrate `exp(x)*sin(x**2 + x)*cos(x)` hangs indefinitely
SymPy cannot solve this type of integrals and instead of returning a `DontKnowRule`, it just keeps trying. The only way to solve this type of integrals is probably to rewrite sins/cos in terms of complex exponentials.

Wolfram Alpha:

<img width="1040" height="345" alt="Image" src="https://github.com/user-attachments/assets/2b9898a9-55b6-4a13-bcc1-003612019ea2" />
Refactor `manualintegrate` into a stateful solver with stateless rules
## Summary

The current architecture of `manualintegrate` relies on recursive rule evaluation, where each rule is responsible for invoking other rules recursively. While this has worked reasonably well, it has become increasingly difficult to extend and has led to several workarounds for problems that stem from the lack of a global solver.

This issue proposes discussing a refactor that separates the integration **solver** from the individual **rules**.

## Motivation

As more integration strategies have been added, several recurring problems have appeared:

* Recursive calls have no knowledge of what has already been attempted.
* Infinite recursion and cyclic rewrites require ad-hoc loop detection.
* Branching decisions must be propagated manually through recursive calls.
* Rules often need to coordinate with each other despite having no shared state.
* Rewriting to alternative forms (e.g. exponentials vs. trigonometric functions) is difficult to manage consistently.

A recent example is PR #30043, where `contextvars` were introduced to propagate the `branch` option through recursive calls made by `integral_steps`. While `contextvars` solve that specific problem (and are thread-safe), they effectively introduce hidden global state to compensate for the current recursive architecture.

This suggests that the underlying issue is architectural rather than specific to branching.

## Proposed architecture

Instead of allowing rules to recursively invoke one another, separate the solver from the rules.

### Rules

Rules should be as stateless as possible.

They simply receive an expression (and any necessary context) and return the next integration step or indicate that they do not apply.

They should not be responsible for recursively solving subproblems or coordinating with other rules.

### Solver

A dedicated solver manages the overall integration process.

Responsibilities could include:

* Dispatching rules
* Managing recursive calls
* Tracking previously-seen expressions
* Preventing infinite recursion
* Limiting or prioritizing branching
* Recording which strategies have already been attempted
* Applying preferred output rewrites (for example converting exponential forms back into trigonometric forms)

This provides a single place to manage solver state instead of distributing it across many rules.

## Benefits

Such a design could eliminate several existing workarounds, including:

* recursive branch propagation via `contextvars`
* scattered loop-detection logic
* repeated attempts of identical transformations
* ad-hoc recursion limits inside individual rules
* limited parsing of integrand and result to rewrite e.g.
```python
    def _has_erf_trig_mul(expr):
        for sub in expr.find(Mul):
            if sub.has(erf, erfc, erfi) and sub.has(sin, cos, sinh, cosh):
                return True
        return False
    if _has_erf_trig_mul(f) and _has_erf_trig_mul(result):
        result = factor_terms(result)
```

It would also make adding new integration strategies simpler, since rules would no longer need to coordinate recursive execution themselves.

## Related work

A similar separation already exists in Franz's @Upabjojr experimental LLM-based integration branch, where rules only produce the forward transformation while the solver manages execution. Although the implementation differs, the overall architecture follows the same principle.

## Backwards compatibility

This proposal concerns the internal architecture of `manualintegrate`.

Maintaining backwards compatibility for internal implementation details is not a goal if doing so significantly complicates the design. The public API and produced integration results should remain unchanged.

## Discussion

Some open questions include:

* What information should the solver track (visited expressions, recursion depth, applied rules, branching history, etc.)?
* Should rules remain pure functions, or should they become lightweight classes with metadata?
* How should rule priority and branching heuristics be represented?
* Can this architecture simplify existing constructs such as `alternatives`, `do_one`, and other recursive combinators?

The goal of this issue is to discuss and agree on the overall architecture before implementing such a refactor.

@asmeurer @oscarbenjamin @Woodman04 
manualintegrate: generator-based rules (yield IntegralInfo) with an IntegrationSolver driving the tree search
## Proposal

Re-architect `manualintegrate` so that **integration rules no longer perform their own recursion**. Today a rule that needs a subintegral solved calls the module-level function directly:

```python
substep = integral_steps(substituted, u)
if substep.contains_dont_know():
    return None
return URule(integrand, symbol, u, u_func, substep)
```

The proposal turns every such rule into a **generator** that *requests* the subproblem from a driver instead of recursing itself:

```python
substep = yield IntegralInfo(substituted, u)
if substep.contains_dont_know():
    return None
return URule(integrand, symbol, u, u_func, substep)
```

A new `IntegrationSolver` object drives the tree search: it dispatches rules on an `IntegralInfo`, and when a rule yields a subproblem, the solver solves it (recursively, through the same machinery) and `send()`s the resulting `Rule` back into the generator at the `yield` expression. A generator may yield any number of times — so a rule can propose further subproblems *after seeing the result of a previous one* — and the assembled `Rule` is the generator's return value. Rules can also yield small request objects other than `IntegralInfo` to read or update per-run solver state (e.g. `PartsUCheck` for the integration-by-parts "u" bookkeeping, `BranchQuery` to ask whether branching is enabled).

Crucially, **all mutable state moves off module globals and onto the solver instance**: the loop-detection set (today `_integral_cache`), the by-parts u-counter (today `_parts_u_cache`), and the options threaded through `integral_steps`.

## Why

1. **The search becomes controllable.** Today the tree search is implicit in the call stack, and nobody owns it. With a solver in charge we get, essentially for free: a `max_depth` limit (`max_depth=1` runs a rule with no subintegrals — ideal for unit-testing rules in isolation), pruning and backtracking policies, cost budgets, and the possibility of alternative strategies (iterative deepening, best-first) without touching any rule.
2. **`AlternativeRule` explosion becomes a switch.** With the driver mediating recursion, a single `branch: bool` option can turn off the collection of alternatives and make the whole engine first-success — a large performance lever for `integrate(..., manual=True)` callers that only want *an* antiderivative, while SymPy Gamma keeps `branch=True` for the pedagogically interesting alternatives.
3. **No module-global state.** `_integral_cache`/`_parts_u_cache` leak between runs and are hostile to threads and reentrancy; solver-owned state makes each integration run self-contained.
4. **Performance pathologies become fixable centrally.** Recent work on new rules (see #30220) showed empirically how rules that spawn nested `integral_steps` calls inside failing search paths can multiply work catastrophically (a slow-test went from 11 s to hours until a guard was added *inside the rule*). With a solver owning the recursion, such policies (budgets, per-rule depth caps, memoized failures) live in one place instead of being re-invented as ad-hoc guards in every rule.
5. **The structural change is mechanical and reviewable.** Converting a rule is a local, pattern-like edit (`... = integral_steps(...)` → `... = yield IntegralInfo(...)`); rules that never recurse are untouched and may keep returning `Rule`/`None` directly — the solver detects generators via `isinstance(result, GeneratorType)` and handles both calling conventions during the transition.

## What this concretely unlocks

Things that are **impossible or ad-hoc today** and become natural once rules are coroutines and a solver owns the search:

* **First-success mode.** Today `alternatives(...)` evaluates *every* applicable rule recursively and each alternative's subtree does the same — work multiplies at every alternative node, even when the caller only wants one antiderivative. With the solver mediating recursion this is a boolean. Measured on PR #30191 (same machine, warm cache, 2 runs):

  | integrand | master | solver, `branch=True` | solver, `branch=False` |
  |---|---:|---:|---:|
  | $\sin^6 x\cos^4 x$ | 1.20 s | 1.91 s | **0.55 s** |
  | $x^3 e^x\sin x$ | 0.13 s | 0.25 s | 0.20 s |
  | $e^x\sin 2x\cos 3x$ | ~38 s | ~61 s | ~52 s |

  2.2× on the alternatives-heavy trig-power case just by not exploring what nobody asked for — and SymPy Gamma keeps `branch=True` because for it the alternatives *are* the product. (The third row is an honest finding for review: the generator conversion is ~35% *slower* there, reproducibly — the cost is not in branching but somewhere in the restructured search path, and it needs profiling before the core PR lands.)

* **Depth budgets and cheap probes.** `IntegrationSolver(max_depth=N)` caps the subproblem tree. Measured: `asin(x)*log(x)` takes ~1.5 s to fully search; with `max_depth=3` the solver answers (here: DontKnow) in ~0.4 s. `max_depth=1` runs a rule with *no* subintegrals at all — which turns rule unit-testing from "run the whole engine and hope" into a real isolated test, and gives rules a cheap way to ask "is this subproblem solvable in one step?" before committing to an expensive path.

* **Global budgets instead of per-rule guards.** During the #30220 work, an end-of-chain rule that spawned nested `integral_steps` on failing search paths took `test_issue_2850` from 11 s to *hours*; the fix was a hand-written applicability guard inside the rule. With the solver owning every recursion, a single node/time budget caps *any* runaway search for *all* rules, present and future — the guard stops being every rule author's responsibility. Timeouts also become clean: every `yield` is a safe interruption point, no signals needed.

* **Memoized subresults.** Today's `_integral_cache` only breaks cycles — the entry is deleted once computed, so identical subintegrals reappearing in sibling branches are recomputed from scratch. A solver can keep completed results for the run and turn the search DAG-shaped, which is precisely where `branch=True`'s multiplicative blowup goes quadratic-instead-of-exponential.

* **Adaptive, conversational rules.** A generator rule can yield a subproblem, *inspect the result*, and then decide what to ask next — several of the newer rules in #30212 already do this (try a reduction, look at what came back, choose the follow-up split). With eager recursion this pattern requires contortions; with coroutines it's just control flow.

* **Schedulable search.** Suspended generators are first-class values: the solver can pause a rule mid-flight, advance a sibling, and come back — enabling best-first orderings, "cheapest alternative first", lazy alternatives for Gamma ("show another way" computed on click, not up front), and eventually parallel exploration of independent branches. None of this is expressible when the search lives on the Python call stack.

* **Uniform observability.** The solver sees every node: per-rule time/node profiling ("which rule burns the budget"), search-tree tracing for debugging, and step counting for the pedagogical output all become one hook instead of scattered `debug()` calls.

## The three implementing PRs

Three recent PRs implement this in increasing scope, and are best read in this order:

1. **#30176 — the structural change alone.** Converts the recursive rules to generators and introduces `IntegrationSolver` (owning `max_depth`, the active-subproblem set for cycle detection, the parts-u counter, and options). No intended behavior change; this is the reviewable core of the proposal. (Originated from the discussion in #30087.)
2. **#30191 — the structural change + `branch: bool`.** Demonstrates how the feature proposed in #30043 (switching off `AlternativeRule`) becomes natural in this architecture, implemented without a `ContextVar` — the flag is plain solver state that rules can query.
3. **#30212 — the full stack.** The solver architecture plus branching `alternatives(*rules, branch=False)`, `BranchQuery`, and a large batch of new rules written natively in the generator style (Weierstrass/Bioche cascade, hyperbolic rational substitution, inverse-function substitution, tabular parts, polylog ladder, `RectifyAtanRule` continuity correction, …). Shows what rule code looks like when written against the new calling convention from the start.

Earlier prototypes (#30107, #30116, #30117) explored where the state should live (stateful solver vs. solver carried by `IntegralInfo`) and moving backtracking/pruning into the solver; #30176 is the distilled form.

## Suggested path

1. Review and land the structural core (#30176-shape) first — mechanical, no behavior change, unlocks everything else.
2. Add the `branch` option (#30191-shape) as the first user-visible payoff.
3. Rebase the rule work (#30212, and the meta-rules discussed in #30220) on top, so new rules are written as generators from the start and search-control policies (budgets, guards) can be enforced by the solver rather than inside each rule.

Discussion welcome — in particular on the request-object protocol (which solver state rules should be able to touch), on whether `max_depth`/budget knobs should be exposed through `integrate(..., manual=True)`, and on the review strategy for the mechanical conversion.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
