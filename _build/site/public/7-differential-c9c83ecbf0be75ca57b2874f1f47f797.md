# 7. Differential of a function

## <span class = "h2-num">7.1 </span><span class = "h2-text"> Implicit differentiation </span>
In high-school, we learned about the *explicit* and *implicit* equation of line:
- explicit form $\displaystyle \quad \dots \quad y = 2x+1$
- implicit form $\displaystyle \quad \dots \quad 2x-y+1 = 0$

The difference between these two forms is that in explicit form we know the formula by which $y$ is given, while in implicit form we don't immediately know that formula (although we can easily compute it). This same method can be used for more general functions.

:::{caution} Example
:icon:false
Consider the function $y(x) = e^x+3.$ This function is given **explicitly** because we are given the formula by which $y$ is given. However, we can preform the following operations:
\begin{equation*}
\begin{split}
y &= e^x+3 \\
e^x &= y-3 \quad / \ln \\
x &= \ln(y-3)
\end{split}
\end{equation*}
and arrive at the expression $x-\ln(y-3) = 0.$ This expression is **implict** form of the function $y$ because we don't immediately know the formula by which the function $y$ is given, but we can easily express $y$ from that equation and find the explicit form.
:::

Sometimes, the implict form of a function can be such that we can't explicitly express $y$ from the given equation. Nonetheless, we know how to compute the derivative of implicitly given function, as the following problems show.

:::{note} Problem 7.1
:icon: false
Let the function $y = y(x)$ be implicitly given by the equation 
\begin{equation*}
x^2+y^2 = 5.
\end{equation*}
Find the derivative $y'$ of the function $y$.
:::

:::{note} Problem 7.2
:icon: false
Let the function $y = y(x)$ be implicitly given by the equation 
\begin{equation*}
x^2 y + y^2 = e^x.
\end{equation*}
Find the derivative $y'$ of the function $y$.
:::

:::{note} Problem 7.3
:icon: false
Let the function $y = y(x)$ be implicitly given by the equation 
\begin{equation*}
x^3 y^2 + y^5 = x^2 e^x+32.
\end{equation*}
If $y(0) = 2,$ find the value of $y'(2).$
:::

## <span class = "h2-num">7.2 </span><span class = "h2-text"> Logarithmic differentiation </span>

## <span class = "h2-num">7.3 </span><span class = "h2-text"> Differential of a function </span>