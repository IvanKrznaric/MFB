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
In the case of functions of one variable, finding the second derivative of a function was easy - you simply take the derivative of the derivative. In case of functions of several variables, this is no longer applicable because the phrase "derivative of the derivative" doesn't have any reasonable meaning: which derivative are we going to differentiate and with respect to which variable?

:::{figure} ./slike/parcijalne-derivacije-2-var.jpg
All the second order partial derivatives of the function $f(x,y).$
:::

:::{figure} ./slike/parcijalne-derivacije-3-var.jpg
All the second order partial derivatives of the function $f(x,y,z).$
:::

:::{note} Problem 10.6
:icon: false
Find all the second order partial derivatives of the function
\begin{equation*}
f(x,y) = 2x^3 -3xy +4y^4.
\end{equation*}
:::

:::{note} Problem 10.7
:icon: false
Let $\displaystyle f(x,y,z) = xe^{y+z^2}.$ Find the the third-order partial derivative $f_{xzz}.$
:::

## <span class = "h2-num">10.3 </span><span class = "h2-text"> Hessian matrix </span>

As we have seen in the previous chapter, if we are given a function of several variables, then there are more than one partial derivative of the second order so we can't speak of a single "second derivative" of such a function. However, we would like to have a single mathematical object that contains all of the second-order partial derivatives of the function $f,$ and the best candidate for such an object is a matrix. Therefore, we define the **<span style = "color: green"> Hessian matrix </span>** of the function $\displaystyle f(x_1, \dots, x_n)$ as
\begin{equation*}
H_f = \begin{bmatrix} f_{x_1, x_1} & \dots & f_{x_1, x_n} \\ \vdots & \dots & \vdots \\ f_{x_n, x_1} & \dots & f_{x_n, x_n} \end{bmatrix}.
\end{equation*}
For example, the Hessian matrix of a function $f(x,y)$ of two variables is given by
\begin{equation*}
H_f (x,y) = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}.
\end{equation*}

The following theorem is of big importance, since it tells us that the Hessian matrix is symmetric. As a consequence, we won't need to explicitly compute all of the second-order partial derivatives since some of the are going to be mutually equal.

:::{danger} <span style = "color: red"> Theorem (Schwartz) </span>
:icon: false
If $f(x_1, \dots, x_n)$ is a given function, then $\displaystyle f_{x_i, x_j} = f_{x_j, x_i}.$
:::
In other words, the order in which you take higher-order partial derivatives does not matter.

:::{note} Problem 10.8
:icon: false
Find the Hessian matrix of the function $\displaystyle f(x,y) = \ln\left(\frac{y}{x^2}\right).$
:::

:::{note} Problem 10.9
:icon: false
Find the Hessian matrix of the function $\displaystyle f(x,y,z) = x^2y - z^3 + xyz$ at the point $(-1,2,0).$
:::

