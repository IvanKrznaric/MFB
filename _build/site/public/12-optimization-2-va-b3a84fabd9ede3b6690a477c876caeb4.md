# 12. Optimization of functions of two variables

## <span class = "h2-num">12.1 </span><span class = "h2-text"> Local extrema </span>

:::{note} ⚙️ How to find the local extrema of a function $f(x,y)$
:icon:false
1. Find the domain of the function $f$
2. Find the partial derivatives $f_x, f_y$
3. Find the points where the partial derivatives are equal to zero, i.e. solve the system 
\begin{equation*}
f_x = 0, \quad f_y = 0
\end{equation*}
3. Use the Hessian matrix to determine the character of the stationary points.
:::
The only thing that's left to answered is how to use the Hessian matrix to determine the character of the stationary points. In order to do so, let
\begin{equation*}
D_1 = f_{xx}, \quad D_2 = \text{det}\left( H_f (x,y)\right).
\end{equation*}
Now we distinguish between three possible cases:
- if $D_2 < 0,$ then $(x,y)$ is a saddle point
- if $D_2 < 0$ and $D_1 > 0,$ then $(x,y)$ is a local minimum
- if $D_2 < 0$ and $D_1 < 0,$ then $(x,y)$ is a local maximum

:::{note} Problem 12.1
:icon: false
Find the local extrema of the function $\displaystyle f(x,y) = x^3 - y^2 - 3x + 12y + 80.$
:::


:::{note} Problem 12.2
:icon: false
Find the local extrema of the function $\displaystyle f(x,y) = \frac{8}{x} + \frac{x}{y} + y.$
:::

:::{note} Problem 12.3
:icon: false
Find the local extrema of the function $\displaystyle f(x,y) = (2x^2-y)\cdot e^{x-y}.$
:::

:::{note} Problem 12.4
:icon: false
A company produces two goods $A$ and $B$, whose prices are set to $p_1, p_2$ respectively. The total cost function is given by
\begin{equation*}
C(Q_1, Q_2) = Q_1^2 + 3Q_2^2 + Q_1 Q_2 + 10,
\end{equation*}
where $Q_1,Q_2$ denote the levels of production of the goods $A,B$. Find the levels of production $Q_1,Q_2$ that maximize the profit function.
:::

## <span class = "h2-num">12.2 </span><span class = "h2-text"> Constrained optimization </span>
In this section we are going to learn how to solve the following problem:
\begin{equation*}
\begin{cases}
\text{optimize:} f(x,y) \\
\text{constraint:} g(x,y) = c
\end{cases}
\end{equation*}