# 9. Elasticity and economic quantities

## <span class = "h2-num">9.1 </span><span class = "h2-text"> Total, average and marginal functions </span>
In this section, we are going to use the following notation:
- **<span style = "color: green">quantity of production </span>** $\dots Q$
- **<span style = "color: green">price</span>** $\dots p$
- **<span style = "color: green">total cost function </span>** $\dots C(Q)$
- **<span style = "color: green">total revenue function </span>** $\dots R(Q)$
- **<span style = "color: green">profit function </span>** $\dots \Pi(Q) = R(Q) - C(Q)$
- **<span style = "color: green">marginal cost function </span>** $\dots MC(Q) = C'(Q)$
- **<span style = "color: green">marginal revenue function </span>** $\dots MR(Q) = R'(Q)$
- **<span style = "color: green">average cost function</span>** $\displaystyle \dots AC(Q) = \frac{C(Q)}{Q}$
- **<span style = "color: green">average revenue function </span>** $\displaystyle \dots AR(Q) = \frac{R(Q)}{Q}$
- **<span style = "color: green">demand function</span>** $\dots q(p)$

:::{note} Problem 9.1
:icon: false
Let the revenue and the total cost function be given by
\begin{equation*}
R(Q) = -5Q^2 + 10Q, \quad C(Q) = 5Q^2 - 90Q.
\end{equation*}
Using this model, find the point of maximum profit and the corresponding maximal value.
:::

:::{note} Problem 9.2
:icon: false
The total cost function of some business model is given by
\begin{equation*}
C(Q) = \frac{Q^2}{100} + 25Q + 100.
\end{equation*}
Find the point of minimum average cost and comupte that minimal value.
:::

:::{note} Problem 9.3
:icon: false
:label: P93
A certain fin-tech startup is developing an app for algorithmic trading and they are modelling their finances in order to plan their future business decisions. Based on the past data, they have used the following functions to model revenue and cost respectively:
\begin{equation*}
R(x) = e^{-x+13} \cdot \left( (x-14)^2+1 \right)+ \frac{x^3}{3} + 225x, \quad C(x) = 15x^2,
\end{equation*}
where the variable $x$ denotes the amount of computing power they are using to power the servers for the app. Based on the model above, find the minimum of the profit function for this startup.
:::

````{solution} P93
:class:dropdown
Since the profit is equal to the difference of the revenue and the cost, we have
\begin{equation*}
\Pi(x) = e^{-x+13} \cdot \left( (x-14)^2+1\right) + \frac{x^3}{3} + 225x - 15x^2.
\end{equation*}
In order to find the minimum, first we have to compute the derivative of the profit function:
\begin{equation*}
\begin{split}
\Pi'(x) &= (e^{-x+13})' \cdot \left((x-14)^2+1\right) + e^{-x+13} \cdot \left( (x-14)^2+1\right)' + x^2 + 225 -30x \\
&= -e^{-x+13} \cdot \left( (x-14)^2+1\right) + e^{-x+13} \cdot(2(x-14)) + x^2-30x + 225 \\
&= -e^{-x+13} \cdot (\left (x-14)^2 -2(x-14) +1 \right) + x^2 -2 \cdot 15 \cdot x + 15^2 \\
&= -e^{-x+13} \cdot \left( x-15\right)^2 + (x-15)^2 \\
&= (x-15)^2 \cdot (-e^{-x+13}+1).
\end{split}
\end{equation*}
Now, the stationary points are given by:
\begin{equation*}
\begin{split}
\Pi'(x) &= 0 \\
\implies (x-15)^2 = 0 &\text{ or } -e^{-x+13}+1 = 0 \\
\implies x = 15 &\text{ or } x = 13.
\end{split}
\end{equation*}
In order to determine which point is a local minimum, we need to compute the second derivative of the function $\Pi$:
\begin{equation*}
\begin{split}
\Pi''(x) &= \left( (x-15)^2 \cdot (-e^{-x+13}+1)\right)' \\
&= 2(x-15) \cdot (-e^{-x+13}+1) + (x-15)^2 \cdot e^{-x+13}.
\end{split}
\end{equation*}
Plugging-in the stationary point $x = 13,$ we get that:
\begin{equation*}
\Pi''(13) &= 4 > 0,
\end{equation*}
so the point $x = 13$ is a local minimum of the profit function.
````

## <span class = "h2-num">9.2 </span><span class = "h2-text"> Elasticity </span>

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
Let $y = y(x)$ be a given function. **<span style = "color:green">The coefficient of elasticity</span>** of $y$ with respect to $x$ is given by 
\begin{equation*}
E_{y,x} = \frac{x}{y} \cdot y'(x).
\end{equation*}
:::

**<span style = "color: magenta">Interpretation </span>** of the coefficient of elasticity is that if the independent variable $x$ increases by $1\%,$ then the value of $y$ will change by approximately $E_{y,x} \%.$

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
Let $y = y(x)$ be a given function. We say that $y$ is
- **<span style = "color: green">inelastic</span>** if $\lvert E_{y,x} \rvert < 1.$
- **<span style = "color: green">elastic</span>** if $\lvert E_{y,x} \rvert > 1.$
- **<span style = "color: green">unit elastic</span>** if $\lvert E_{y,x} \rvert = 1.$
- **<span style = "color: green">perfectly inelastic</span>** if $E_{y,x} = 0.$
- **<span style = "color: green">perfectly elastic</span>** if $\lvert E_{y,x} \rvert = \infty.$
:::

:::{note} Problem 9.4
:icon: false
Given the demand function $\displaystyle q(p) = \frac{100}{(p+2)^2},$ calculate the elasticity at the level $p = 2$ and interpret the result.
:::

:::{note} Problem 9.5
:icon: false
Given the demand function $\displaystyle q(p) = \frac{100-p^2}{3},$ find the intervals over which the demand is elastic and inelastic.
:::

:::{note} Problem 9.6
:icon: false
Given the elasticity of the total cost function $\displaystyle E_{C,Q} = \frac{Q}{\sqrt{Q+2}},$ find the level of production for which the average cost is equal to the marginal cost.
:::

:::{note} Problem 9.7
:icon: false
Given the elasticity of the average cost function
\begin{equation*}
E_{AC,Q} = e^{2Q+7} - \sqrt{\ln(Q+500)},
\end{equation*}
find the elasticity of the total cost function.
:::

:::{note} Problem 9.8
:icon: false
:label: P98
Determine all values of parameter $t \in \mathbb{R}$ such that the function $\displaystyle f(x) = xe^{(t+1)x}$ is inelastic at the level $x = 1.$
:::

````{solution} P98
:class: dropdown
So, if we want the function $f$ to be inelastic at the level $x = 1,$ then we need to compute the coefficient of elasticity, plug-in $x = 1$ and find the the absolute value of the expression we got is less than $1$. 

First, let's compute the coefficient of elasticity:
\begin{equation*}
\begin{split}
E_{f,x} &= \frac{x}{f} \cdot f' \\
&= \frac{x}{xe^{(t+1)x}} \cdot (x \cdot e^{(t+1)x})' \\
&= \frac{1}{e^{(t+1)x}} \cdot (e^{(t+1)x} + x \cdot e^{(t+1)x} \cdot (t+1)) \\
&= \frac{1}{e^{(t+1)x}} \cdot e^{(t+1)x} \cdot (1+x(t+1)) \\
&= 1+x(t+1).
\end{split}
\end{equation*}
At the level $x = 1$ we have $E_{f,x}(1) = t+2.$

Now, we want to absolute value of the coefficient of elasticity to be less than $1$, so:
\begin{equation*}
\begin{split}
\lvert E_{f,x} \rvert &< 1 \\
\implies \lvert t+2 \rvert &< 1 \\
\implies -1 &< t+2 < 1 \\
\implies -3 &< t < -1.
\end{split}
\end{equation*}
So, in order for the function $f$ to be inelastic at the level $x = 1,$ the parameter $t$ has to belong to the interval $\langle -3, -1 \rangle.$ \hfill $\blacksquare$
````