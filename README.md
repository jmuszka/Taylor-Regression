# Taylor Regression

A calculus-based approach to nonlinear regression.

## Introduction

Back in June of 2024, I set out to begin learning more about machine learning. In particular, I was inspired by the curve-fitting problem: given an arbitary set of points on a plane, can we generalize a function to adequately approximate the outputs and interpolate the values between them?

Before formally diving into my study of the field of statistical learning methods, I decided to have a go at this problem myself. I devised an algorithm derived from Taylor's Theorem using Gauss-Jordan elimination, and a demonstration is implemented in Python with pandas and numpy matrix solver.

In the next section I explain how I derived the algorithm, its performance, its limitations, and potential future endeavors. The underlying math is not too complicated, merely depending on some knowledge of one-dimensional calculus, linear algebra, and statistics; remember - I made this before formally studying more practical data science methods.

## Algorithm


Let us introduce Taylor's Theorem. We'll spare the rigor and simply work with an informal definition:

$\displaystyle f(x) \doteq P(x, n) = \sum_{k=0}^na_k x^k$, where $x \in \mathbb{R}$ belongs to the function's domain, $n \in \mathbb{N}_0$ is the desired degree of the approximating polynomial, and $a$ is some sequence of real numbers.

What this means is that any continuous real-valued function (more precisely, *smooth analytic function*) can be approximated by an arbitary polynomial. Note that Taylor's Theorem proves that $P$ converges exactly to $f$ as $n \to \infty$ within a certain *interval of convergence*; while this extends beyond the scope of this derivation, it is nonetheless a fact that will be of importance later.

In other words, for all $ (x,\, f(x))$ is a given set of points,  $\exists \,n \in \mathbb{N}_0$ such that $f(x) = P(x,n) \pm \varepsilon$, for some acceptable error $\varepsilon$. From here, we must determine an algorithm to compute the coefficients $a_k$ of polynomial $P$.

Let $A$ be the set of points that we are to interpolate. With each $(x_i, f(x_i)) \in A$, we construct a system of linear equations:

$f(x_0) = a_0+a_1x_0 + \dots + a_nx_0^n$

$f(x_1) = a_0+a_1x_1 + \dots + a_nx_1^n$

$\vdots$

$f(x_i) = a_0+a_1x_i + \dots + a_nx_i^n$

$\vdots$

By Rouché–Capelli Theorem (this is just a fancy name for finding the solution of a matrix in reduced row echelon form), if there exists $i$ in each row such that $a_i \neq 0$, or, in the case that each coefficient in row $i$ is $0$, then $f(x_i)=0$, then there exists an $n$-degree polynomial for the set of points $A$. Solving this system of equations will yield the coefficients for polynomial $P$, which will map the points in $A$ and interpolate between them.\*

## Result

Now we have an algorithm that for any $(x,\, y)$ pair in the given set of points can compute exactly\* $P(x) = y$; and since the polynomial is continuous, we have a robust method to estimate the relationship between the given points. Not only does this solve the curve-fitting problem, but this algorithm is a form of nonlinear regression that can, in theory, be applied to statistical learning contexts.

You'll notice we've been putting an asterisk on the fact that this function can compute the given points. This hinges on the fact that $P$ is actually an *approximation* of $f$ dependent on the chosen degree $n$ of the polynomial, since in computational mathematics we cannot perform infinite arithmetic. Remember earlier how we mentioned the concept of an interval of convergence? It turns out that our finite polynomial only converges to the given points within a small interval centered at $x=0$, dependent on our chosen $n$. For values of $x$ outside this range, our model cannot make reasonable inferences.

Now, this is fine if we want to interpolate strictly *between* the points, but this limits our ability to make predictions beyond the maximum and minimum $x$ values of the set of points - a feature that may be desired in a statistical learning context.

Furthermore, we run into problems beyond the calculus portion of this algorithm. With $m$ points on a graph and a chosen degree of $n$, our algorithm is going to compute without fail a polynomial of degree $\min(n,\,m)$. Firstly, if $m >n$, then $P$ will invariably "miss out" on including some of the points on its curve, since the polynomial will not be of high enough degree to capture the level of variance in the input data. Secondly, in the case that $m \leq n$, and especially when $m < n$, while $P$ will cover each of the points with 100% accuracy, this high-degree polynomial is a naive solution with very high variance. Not only is this a computationally expensive method (relatively speaking), it sacrifices the quality of our inferences when in reality we would be perfectly fine with allowing a small margin of error in exchange for a more "reasonable" and efficient function. In machine learning, this dilemma is referred to as the *bias-variance tradeoff*.

## Reflection

All in all, we end up with a satisfactory algorithm that can fit a function to an arbitary set of points. Is this the most efficient solution? No. Far from it, in fact. But given that there are entire fields of study related to this very problem, and the fact that I hacked together this algorithm and implementation in the span of a couple hours, this is a fairly satisfying result.

Overall, I am glad that I decided to embark on this experiment. This endeavor has expanded my intuition regarding statistical learning and data science more broadly. There are certainly some ways which I could improve this method, such as accounting for an error tolerance, and determining the lowest possible degree of polynomial that does not trade off much accuracy. Realistically, however, my time would be better spent stuyding legitimate data science techniques that supersede the limitations of this rudimentary curve-fitting model.

## Further Reading

Calculus:
- [Taylor's Theorem](https://en.wikipedia.org/wiki/Taylor_series)
- [Curve Fitting](https://math.libretexts.org/Courses/Angelo_State_University/Mathematical_Computing_with_Python/3%3A_Interpolation_and_Curve_Fitting/3.1%3A_Introduction_to_Interpolation_and_Curve_Fitting)
- [Smooth Analytic Functions](https://math.stackexchange.com/questions/874820/what-is-the-difference-between-the-terms-smooth-analytical-and-continuous)

Statistical Learning:
- [Nonlinear Regression](https://en.wikipedia.org/wiki/Nonlinear_regression)
- [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)

Linear Algebra:
- [Rouché–Capelli Theorem](https://en.wikipedia.org/wiki/Rouch%C3%A9%E2%80%93Capelli_theorem)