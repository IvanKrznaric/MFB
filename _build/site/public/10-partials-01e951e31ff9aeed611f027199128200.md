# 10. Partial derivatives

## <span class = "h2-num">10.1 </span><span class = "h2-text"> Partial derivatives </span>
In this section, we are going to learn how to find differentiate functions of several variables. The definition os such a derivative is analogous to the case of functions of one variable.

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
Let $f(x,y)$ be a function of two variables. If, for a fixed value of $x$, the limit 
\begin{equation*}
\lim_{h \to 0} \frac{f(x,y+h)-f(x,y)}{h}
\end{equation*}
exists, then we say that the value of that limit is the **<span style = "color: green"> partial derivative </span>** of the function $f$ with respect to the variable $y$ and that limit is denoted by $f_y.$ <br>
In the same way, we define the partial derivative $f_x.$
:::

As we'll see in the problems that follow, in pratice this means that the same rules and formulas that we have previously learned in case of functions of one variable apply in the case of functions of several variables as well.

:::{note} Problem 10.1
:icon: false
Find the partial derivatives of the function $\displaystyle f(x,y) = 3x^2 + xy + \sqrt{y}.$
:::

:::{note} Problem 10.2
:icon: false
Find the partial derivatives of the function $\displaystyle f(x,y) = (x^2+y+4) \cdot e^y.$
:::

:::{note} Problem 10.3
:icon: false
Find the partial derivatives of the function $\displaystyle f(x,y) = \frac{2x-y}{x+y}.$
:::

:::{note} Problem 10.4
:icon: false
Find the partial derivatives of the function $\displaystyle f(x,y) = e^{-2x^2-4y^2+5x+3y}.$
:::

:::{note} Problem 10.5
:icon: false
Find the partial derivatives of the function $\displaystyle f(x,y,z) = e^{2xz}-\ln(yz) +1.$
:::

## <span class = "h2-num">10.2 </span><span class = "h2-text"> Higher-order partial derivatives </span>
In the case of functions of one variable, finding the second derivative of a function was easy - you simply take the derivative of the derivative. In case of functions of several variables, this is no longer applicable because the phrase "derivative of the derivative" doesn't have has any reasonable meaning: which derivative are we going to differentiate and with respect to which variable?

## <span class = "h2-num">10.3 </span><span class = "h2-text"> Hessian matrix </span>


