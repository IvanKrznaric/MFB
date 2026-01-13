# 15. Differential equations

## <span class = "h2-num">15.1 </span><span class = "h2-text"> Introduction </span>
When we were in elementary school, we were taught how to solve linear equations like
\begin{equation*}
-2x+17 = 8x-13.
\end{equation*}
The algorithm started with us moving all of the unknows to the one side, all of the knows to the other side and then explicitly solving the equation for $x$. In what follows, we will introduce a new kind of an equation and then we will try and see which of the steps from the algorithm for solving linear equations can be used to solve this new type of an equation.

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
**<span style = "color : green"> A differential equation </span>** is any equation that is given in terms of the derivative of an unknown function $y$, expressions that contain independent variable $x$ and constants.
:::

:::{caution} Example
:icon: false
- Equation $y' = 7$ is a differential equation since it is given in terms of the derivative of some unknown function $y$
- Equation $x \cdot y' = 2\sqrt{x} - 1$ is a differential equation since it is given in terms of the derivative of some unknown function $y$
- Equation $y^2 = 9$ is not a differential equation sice it is not given in terms of the derivative of some unknown function
:::

Now, our goal is to come up with an algorithm that we'll be able to use for solving differential equations. As mentioned before, we will use the algorithm for solving linear equations and try to adapt its steps. So, in order to solve the linear equation given above, we have the following:

\begin{equation*}
\begin{split}
-2x + 17 &= 8x - 13 \\
-2x - 8x &= -13 - 17 \quad [\text{\small separate the unknows from the knowns}] \\
-10 x &= - 30 / \colon (-10) \quad [\text{\small express the unknown}] \\
x &= 3
\end{split}
\end{equation*}

Take, for example, the differential equation $\displaystyle x \cdot y' = 2\sqrt{x} - 1$. From the algorithm above, the first step in solving this differential equation would be to **<span style = "color : red"> separate the unkowns from the knowns </span>**. Since we consider the function $y$ to be unknown, while the variable $x$ and all of the constants are know, we get the following:

\begin{equation*}
y' = \frac{2\sqrt{x} - 1}{x}.
\end{equation*}

Based on the algorithm for solving linear equations, the next step should be to **<span style = "color : red"> express the unknown.</span>** In case of linear equations, we have expressed the unknown variable $x$ by dividing the whole equation by $-10$ since division is the opposite operation to multiplication. Similarly, in case of differential equations we have to integrate since integration is the opposite operation to differentiation. Hence, the algorithm for solving differential equations can be summarized as follows:

:::{note} ⚙️ Solving differential equations
:icon: false
- Separate the unknowns from the knowns
- Integrate
:::

Lastly, let's compare linear and differential equations side by side:

\begin{equation*}
\begin{array}{| c | c | c |}
& -2x+17 = 8x - 13 & x \cdot y' = 2\sqrt{x} - 1 \\
\hline
\text{\small type of equation} & \text{\small linear} & \text{\small differential} \\
\text{\small knowns} & \text{\small constants} & \text{\small constants and expressions containing } x \\
\text{\small unknowns} & x & y 
\end{array}
\end{equation*}

:::{prf:remark}
:numbered: false
When solving linear equations, then there is only one possible solution (for example, in the linear equation considered above the only solution is $x = 3$). On the other hand, differential equations have infinitely many solutions. For example, one possible solution to the differential equation $y' = 7$ is the function $y(x) = 7x$ since $y' = 7$, but the functions
\begin{equation*}
y(x) = 7x + 1, \quad y(x) = 7x + 100, \quad y(x) = 7x - 1013
\end{equation*}
are also its solutions since they all satisfy $y' = 7$. Therefore, adding a constant to a solution does not affect the result, and that is indicated by writing "$+C$" in the solution.
:::

## <span class = "h2-num">15.2 </span><span class = "h2-text"> Solving differential equations </span>

:::{note} Problem 15.1
:icon: false
Solve the differential equation $\displaystyle x \cdot y' = 2\sqrt{x} - 1$.
:::

:::{note} Problem 15.2
:icon: false
Solve the differential equation $\displaystyle y' + xy - 3y = 0$.
:::

:::{note} Problem 15.3
:icon: false
Find all functions $y(x)$ such that
\begin{equation*}
\begin{cases}
E_{y,x} = x+1 \\
y(1) = 2e
\end{cases}
\end{equation*}
:::

:::{note} Problem 15.4
:icon: false
The rate at which the purchasing power of a currency changes over time is modelled by the differential equation
\begin{equation*}
2\sqrt{2x+1} \cdot P' -1 = 0,
\end{equation*}
where $x$ represents time measured in years and $P(x)$ represents the purchasing power of a currency at time $x$. <br>
If the initial purchasing power is equal to $3/4$, find the time needed for the purchasing power of the currency to reach $23/4$.
:::
