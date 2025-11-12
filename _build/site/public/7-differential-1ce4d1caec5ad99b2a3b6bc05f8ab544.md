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

:::{note} Problem 7.4
:icon: false
Let the function $y = y(x)$ be implicitly given by the equation 
\begin{equation*}
3x^3+2y^2 = 3x+y.
\end{equation*}
If $\displaystyle y(1) = \frac{1}{2},$ find the value of $y'(1).$
:::

## <span class = "h2-num">7.2 </span><span class = "h2-text"> Logarithmic differentiation </span>
So far, we know how to find the derivatives of products, quotients, compositions and implicitly given functions. However, there are still some functions that we don't (yet) know how to differentiate. In this section, we will learn a new method that we'll be able to use to differentiante some functions.

:::{note} Problem 7.5
:icon: false
Find the derivative of the function $\displaystyle f(x) = x^{x+1}.$
:::

:::{note} Problem 7.6
:icon: false
Find the derivative of the function $\displaystyle f(x) = (x^2-6x+3)^{\sqrt{x+7}}.$
:::

:::{note} Problem 7.7
:icon: false
Let $\displaystyle f(x) = (x-5)^\frac{e^{x^2}}{2}.$ Find the value of $f'(6).$
:::

## <span class = "h2-num">7.3 </span><span class = "h2-text"> Differential of a function </span>
Remember that the derivative of the function $f$ is defined as the limit
\begin{equation*}
f'(x) = \lim_{h \to 0} \frac{f(x+h)-f(x)}{h}.
\end{equation*}

If $h$ is very very close to $0$, then it follows that 
\begin{equation*}
\label{approx}
f(x+h)-f(x) \approx f'(x) \cdot h.
\end{equation*}

This approximation is very important to us, so we want to give special names to the variables above:

- **<span style = "color: green"> small displacement</span>** $\dots dx = h$
- **<span style = "color:green"> exact change </span>** $\dots \Delta f(x_0) = f(x_0 + dx)-f(x_0)$
- **<span style = "color:green"> the differential </span>** $\dots df(x_0) = f'(x_0) \cdot dx.$

Therefore, the [equation above](#approx) tells us that 
\begin{equation*}
\Delta f(x_0) \approx df(x_0).
\end{equation*}
In other words, **<span style = "color:red">the exact change in the value of the function can be approximated by the differential.</span>**

Of course, the approximation can be accurate or not, so we need a way of measuring the error we make when using the differential to approximate the exact change:
- **<span style = "color:green"> absolute error </span>** $ \displaystyle \dots \lvert \Delta f(x_0) - df(x_0)\rvert$
- **<span style = "color:green"> relative error </span>** $\displaystyle \dots \frac{\lvert \Delta f(x_0) - df(x_0)\rvert}{\Delta f(x_0)}$