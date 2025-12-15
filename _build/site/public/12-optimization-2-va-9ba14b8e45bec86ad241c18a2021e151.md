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

The only thing that's left to be answered is how to use the Hessian matrix to determine the character of the stationary points. In order to do so, let
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
\text{optimize: } \quad f(x,y) \\
\text{constraint: } \quad g(x,y) = c
\end{cases}
\end{equation*}
There are two ways in which we can solve the problem above:
- substitution method
- Lagrange multiplier method

### ~ Substitution method ~
**<span style = "color:blue"> Substitution method </span>** is extremely useful when the constraint is given in the form of a linear function.

:::{note} Problem 12.5
:icon: false
Find the local extrema of the function $\displaystyle f(x,y) = e^{xy}$ given the constraint $x+y = 4.$
:::


:::{note} Problem 12.6
:icon: false
A company's cost function is modeled by the function 
\begin{equation*}
C(L,K) = 2L + K + 10,
\end{equation*}
where $L,K$ denote the amount of labour and invested capital respectively. The production is given by $Q(L,K) = LK.$ Find the levels of $L$ and $K$ at which the minimum of cost function is achieved when the production is fixed at $8$ units.
:::

:::{note} Problem 12.7
:icon: false
The consumer wants to buy $x$ amount of product $A$ and $y$ amount of product $B$. The utility of those products, depending on the amount bought, is given by
\begin{equation*}
u(x,y) = 2x + 2xy + y.
\end{equation*}
Price of product $A$ is $p_1 = 2$ euros per unit, while the price of product $B$ is $p_2 = 1$ euro per unit.
- If the consumer can spend only $20$ euros, write down the constraint
- Given that constraint, maximize the utility function
:::


:::{note} Problem 12.8
:icon: false
A tech startup is modelling how its stock price depends on its investments in $R\&D$ and its investments in marketing. The amount of money spent on $R\&D$ is denoted by $x$ and the amount of money spent of marketing is denoted by $y$, both measured in thousands of dollars. Analysts model the stock price as
\begin{equation*}
f(x,y) = e^{-2x^2-4y^2+5x+3y}.
\end{equation*}
If the company plans to allocate $40$ thousand dollars between $R\&D$ and marketing, determine the optimal allocation of funds between $R\&D$ and marketing so that the company maximizes the value of its stock.
:::

### ~ Lagrange multiplier method ~
As we have seen in the previous problems, substitution method is very useful when the constraint is such that we can express one variable via the other, but we need a method for problems when that is not the case.