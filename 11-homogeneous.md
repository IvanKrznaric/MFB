# 11. Homogeneous functions

## <span class = "h2-num">11.1 </span><span class = "h2-text"> Homogeneous functions </span>

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
We say that a function $f(x_1, \dots, x_n)$ is **<span style = "color:green">homogeneous</span>** if 
\begin{equation*}
f(\lambda x_1, \dots, \lambda x_n) = \lambda^\alpha \cdot f(x_1, \dots, x_n),
\end{equation*}
where $\alpha \in \mathbb{R}$ is some number, which we call **<span style = "color:green">degree of homogeneity.</span>**
:::

**<span style = "color: magenta">Interpretation </span>** of the degree of homogeneity is that if all variables increase by $1\%,$ then the function $f$ will change its value by approximately $\alpha \%.$

:::{note} Problem 11.1
:icon: false
Check whether or not the function $\displaystyle f(x,y) = x^2 + 2xy + 3y^2$ is homogeneous.
:::

:::{note} Problem 11.2
:icon: false
Check whether or not the function $\displaystyle f(x,y,z) = 2x \cdot \ln\left(\frac{z}{y}\right)$ is homogeneous.
:::

:::{note} Problem 11.3
:icon: false
The Cobb-Douglas production function is given as
\begin{equation*}
Q(L,K) = c L^a K^b,
\end{equation*}
where $a,b,c$ are just some constants. Check whether or nor the Cobb-Douglas production function is homogeneous.
:::

:::{note} Problem 11.4
:icon: false
Let the Cobb-Douglas function be given as 
\begin{equation*}
Q(L,K) = 0.2 L^{0.3} K^{0.6}.
\end{equation*}
If both variables $L,K$ increase by $5\%,$ by how much will the production function $Q$ change its value?
:::

:::{note} Problem 11.5
:icon: false
Let $\displaystyle f(x,y) = x \cdot \sqrt[3]{\frac{x^4 + 5x^2y^2+4y^4}{2x+y}}.$ <br>
For how many percent will the value of the function $f$ change is both of the variables $x,y$ decrease by $7\%?$
:::

## <span class = "h2-num">11.2 </span><span class = "h2-text">Partial elasticities </span>

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
Let $f(x,y)$ be a given function. **<span style = "color:green"> Partial elasticity of the function $f$ with respect to the variable $x$</span>** is given by
\begin{equation*}
E_{f,x} = \frac{x}{f} \cdot f_x.
\end{equation*}
Analogously, **<span style = "color:green"> partial elasticity of the function $f$ with respect to the variable $y$</span>** is given by
\begin{equation*}
E_{f,y} = \frac{y}{f} \cdot f_y.
\end{equation*}
:::

**<span style = "color: magenta">Interpretation </span>** of the partial elasticities is the same as it was in the case of functions of one variable - for example, if the variable $x$ increases by $1\%$ and the value of $y$ remains the same, then the value of the function $f$ changes by approximately $\lvert E_{f,x} \rvert \%.$

:::{note} Problem 11.6
:icon: false
Let $\displaystyle f(x,y) = \sqrt{x-y^2}.$ <br>
- Find the partial elasticities of the function $f$
- Compute the values of partial elasticities of the function $f$ at $x = 25, y = 3$ and interpret the results.
:::

As we'll see in the following problems, partial elasticities have an important economic application.

:::{figure} ./slike/partial-elasticities.jpg
The market with two goods, where each one of them has its own price, demand and elasticity.
:::

We will be refering to the elasticities $E_{q_1, p_2}$ and $E_{q_2, p_1}$ as **<span style = "color:green">cross-price elasticities,</span>** as they tell us what happens to the demand of one good if the price of another good increases. On the other hand, we will be reffering to the elasticities $E_{q_1, p_1}$ and $E_{q_2, p_2}$ simply as **<span style = "color:green">price elasticities,</span>** since they only tell us what happens to the demand of a good if its own price increases.

Based on the value of the cross-price elasticities, we have the following categorization of goods on a market:
- if $\displaystyle E_{q_2, p_1} > 0,$ then the goods are **<span style = "color:green"> substitutes </span>**
- if $E_{q_2, p_1} < 0,$ then the goods are **<span style = "color:green"> complements </span>**

:::{note} Problem 11.7
:icon: false
There are two goods $A$ and $B$ on the market, whose prices are $p_1, p_2$ respectively. The demand for one of those goods is given by
\begin{equation*}
q(p_1, p_2) = \frac{1}{2}p_1^2 + \frac{5}{p_2}.
\end{equation*}
Find the coefficients of price and cross-price elastiticities at $p_1 = 1, p_2 = 2.$ Are these two goods substitutes or complements?
:::

:::{note} Problem 11.8
:icon: false
In a global card payment market, two transaction processing companies $A$ and $B$ are selling their services. Company $A$ is chargin the price $p_1$ per transaction and company $B$ is charging $p_2$ per transaction. The demand for the services of the company $B$ is modelled by the function
\begin{equation*}
q_2(p_1, p_2) = \frac{1}{4}p_1^4+5p_2.
\end{equation*}
- Find the price and cross-price elasticity of that demand.
- If company $B$ is charging $p_2 = 25$ units per transaction, for what prices can company $A$ charge the transactions so that the services these companies offer are substitutes?
:::

## <span class = "h2-num">11.3 </span><span class = "h2-text">Euler's Theorem</span>
In this section, we are going to see what is the relationship between homogeneous functions and partial elasticities.

:::{danger} <span style = "color: red"> Theorem (Euler) </span>
:icon: false
:label: THMEuler
Let $f(x_1, \dots, x_n)$ be a given function. <br>
If the function $f$ is a homogeneous function with degree $\alpha,$ then
\begin{equation*}
x_1 f_{x_1} + \dots + x_n f_{x_n} = \alpha f.
\end{equation*}
:::
Notice that the equation in [Euler's Theorem](#THMEuler) is equivalent to
\begin{equation*}
E_{f, x_1} + \dots + E_{f,x_n} = \alpha.
\end{equation*}

:::{note} Problem 11.9
:icon: false
Let $\displaystyle f(x,y) = \frac{y^3}{x^2} \ln \left(\frac{x(y-x)}{y^2}\right).$ Compute $\displaystyle x f_x + y f_y.$
:::

:::{note} Problem 11.10
:icon: false
Let the production function of some good be given by 
\begin{equation*}
Q(L,K) = \sqrt{\frac{L^4 + K^4}{LK}},
\end{equation*}
where $L$ denotes the amount of labour and $K$ denotes the amount of invested capital.
- Find the sum of partial elasticites of the function $Q$
-  If both the amount of labour and invested capital increase by $5\%,$ by how much will the production increase?
- Assume that $E_{Q,L}(1,1) = 1/2.$ How will the increase of invested capital by $1\%$ at the level $L = 1, K = 1$ affect the production?
:::


:::{note} Problem 11.11
:icon: false
Companies $A$ and $B$ provide the service of making financial models for various industries. Company $A$ charges $p_1$ for its services, while the company $B$ charges $p_2.$ Price elasticity of the demand $q_2$ for the services of company $B$ is given by
\begin{equation*}
E_{q_2, p_2} = \frac{p_1^4 + p_2^6 -5p_1^2+p_2^3}{p_1^4+p_2^6}.
\end{equation*}
- If the demand $q_2(p_1, p_2)$ is homogeneous of degree $1$, find the cross-price elasticity $E_{q_2, p_1}.$
- If the company $B$ charges $p_2 = 5$ units for its services, determine all prices for which the company $A$ can charge its services so that these services are complements.
:::

