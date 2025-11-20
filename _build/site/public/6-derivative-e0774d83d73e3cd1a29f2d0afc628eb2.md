# 6. Derivative of a function

## <span class = "h2-num">6.1 </span><span class = "h2-text"> Introduction </span>

:::{caution} <span style = "color:#8B4000"> Example </span>
:icon: false
Imagine you have invested some amount of money into a bond fond, and the value $V$ of your investment depends on the interest rate $r$, so that $V = V(r).$ Suppose that the interest rate slightly increases from $r$ to $r+h,$ where $h$ is some small number.
- How can you approximate the change in your investment value due to this small increase in interet rate?
- How can you express the average rate of change of the investment value?
- What happens to this average rate of change as the change in interest rate becomes very very small?
:::

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
Let $f : I \rightarrow \mathbb{R}$ be a function. If it exists, the limit
\begin{equation*}
\lim_{h \to 0} \frac{f(x+h)-f(x)}{h}
\end{equation*}
is called **<span style = "color:green"> the derivative </span>** of the function $f$ at a point $x$. We denote this limit by $f'(x).$
:::

:::{figure} ./video/Derivative.mp4
Visual interpretation of the derivative - the derivative of a function $f$ at a point $x$ is equal to the slope of the tangent line to the graph of the function $f$ at a point $x$.
:::

## <span class = "h2-num">6.2 </span><span class = "h2-text"> Derivative of elementary functions </span>


:::{danger} <span style = "color:red"> Basic rules for differentiation</span>
:icon:false
:class: dropdown
\begin{align*}
(f+g)' &= f' + g' & & & & & (c \cdot f)' &= c \cdot f' \\
(f \cdot g)' &= f' \cdot g + f \cdot g' & & & & & \left( \frac{f}{g}\right)' &= \frac{f' \cdot g - f \cdot g'}{g^2} \\
\end{align*}
:::

:::{danger} <span style = "color:red"> Table of derivatives </span>
:icon:false
:class:dropdown
\begin{align*}
c' &= 0 & & & & & (x^n)' &= n \cdot x^{n-1} & & & & & (\sqrt{x})' &= \frac{1}{2\sqrt{x}}\\
(a^x)' &= a^x \cdot \ln(a) & & & & & (e^x)' &= e^x & & & & & (\ln(x))' &= \frac{1}{x}
\end{align*}
:::

:::{note} Problem 6.1
:icon: false
Find the derivative of the function $f(x) = x^3+x+125.$
:::

:::{note} Problem 6.2
:icon: false
Find the derivative of the function $f(x) = (x+1) \cdot (3x^2+2).$
:::

:::{note} Problem 6.3
:icon: false
Find the derivative of the function $\displaystyle f(x) = \frac{x^2}{x+1}.$
:::

:::{note} Problem 6.4
:icon: false
Find the derivative of the function $\displaystyle f(x) = 3x \cdot 3^x.$
:::

:::{note} Problem 6.5
:icon: false
Find the derivative of the function $\displaystyle f(x) = \frac{2^x \cdot (5x+7)}{x^2+5} \cdot \sqrt{x}.$
:::

## <span class = "h2-num">6.3 </span><span class = "h2-text"> Derivative of composition of functions </span>

The following formula tells us how to find derivative of compositions:
:::{danger} <span style = "color:red"> Derivative of a composition of functions</span>
:icon:false
\begin{equation*}
f(g(x))' = f'(g(x)) \cdot g'(x). 
\end{equation*}
:::
Therefore, in order to find the derivative of a composition of functions you move from the "outside" to the "inside" and write the derivatives as you go along.

:::{note} Problem 6.6
:icon: false
Find the derivative of the function $\displaystyle f(x) = (2x+1)^{2025}.$
:::

:::{note} Problem 6.7
:icon: false
Find the derivative of the function $\displaystyle f(x) = \frac{1}{\sqrt{1-2x^4}}.$
:::

:::{note} Problem 6.8
:icon: false
Find the derivative of the function $\displaystyle f(x) = 4^{\sqrt{1-x^3}}.$
:::

:::{note} Problem 6.9
:icon: false
Find the derivative of the function $\displaystyle f(x) = \ln \left( \frac{x}{1-x}\right).$
:::

:::{note} Problem 6.10
:icon: false
Find the derivative of the function $\displaystyle f(x) = x^2 \cdot e^{x \cdot \sqrt{x}}.$
:::

## <span class = "h2-num">6.4 </span><span class = "h2-text"> Derivative via the definition </span>

:::{note} Problem 6.11
:icon: false
Using the definition, find the derivative of the function $\displaystyle f(x) = 17.$
:::

:::{note} Problem 6.12
:icon: false
Using the definition, find the derivative of the function $\displaystyle f(x) = 5x+7.$
:::

:::{note} Problem 6.13
:icon: false
Using the definition, find the derivative of the function $\displaystyle f(x) = 2x^2+3x-130.$
:::

:::{note} Problem 6.14
:icon: false
Using the definition, find the derivative of the function $\displaystyle f(x) = x^3.$
:::

:::{note} Problem 6.15
:icon: false
Using the definition, find the derivative of the function $\displaystyle f(x) = \sqrt{x}.$
:::

## <span class = "h2-num">6.5 </span><span class = "h2-text"> Higher-order derivatives </span>

:::{note} Problem 6.16
:icon: false
Find the first, second and the third derivative of the function $f(x) = 4x \cdot \ln(x).$ 
:::

:::{note} Problem 6.16
:icon: false
Find the first, second and the third derivative of the function $\displaystyle f(x) = \frac{2+x}{2-x}.$ 
:::
