# 9. Elasticity and economic quantities

## <span class = "h2-num">9.1 </span><span class = "h2-text"> Total, average and marginal functions </span>
In this section, we are going to use the following notation:
- **<span style = "color: green">quantity of production </span>** $\dots Q$
- **<span style = "color: green">price</span>** $\dots p$
- **<span style = "color: green">total cost function </span>** $\dots C(Q)$
- **<span style = "color: green">total revenue function </span>** $\dots R(Q)$
- **<span style = "color: green">profit function </span>** $\dots \Pi(Q) = R(Q) - C(Q)$
- **<span style = "color: green">marginal cost function </span>** $\dots MC(Q) = T'(Q)$
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
A certain fin-tech startup is developing an app for algorithmic trading and they are modelling their finances in order to plan their future business decisions. Based on the past data, they have used the following functions to model revenue and cost respectively:
\begin{equation*}
R(x) = e^{-x+13} \cdot \left( (x-14)^2+1 \right)+ \frac{x^3}{3} + 225x, \quad C(x) = 15x^2,
\end{equation*}
where the variable $x$ denotes the amount of computing power they are using to power the servers for the app. Based on the model above, find the minimum of the profit function for this startup.
:::


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