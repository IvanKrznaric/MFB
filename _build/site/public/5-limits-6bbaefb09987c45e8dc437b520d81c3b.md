# 5. Domains and limits of functions

## 5.1 Domain of a function

:::{tip} Definition
:icon:false
**Domain** of the function $f$ is the set of all real numbers $x$ for which that function is defined. Such as set is denoted by $\mathcal{D}_f.$
:::

:::{note} Problem 5.1
:icon:false
Find the domains of the following functions:
- $\displaystyle f(x) = 3x^2 -5x + 9$
- $\displaystyle f(x) = \sqrt{x+9}$
- $\displaystyle f(x) = \sqrt[3]{x+7}$
- $\displaystyle f(x) = \frac{-2x^2+x+1}{x^2+x-6}$
- $\displaystyle f(x) = \ln(x-3)$
:::

:::{note} Problem 5.2
:icon:false
Find the domains of the following functions:
- $\displaystyle f(x) = \ln\left(\frac{x+1}{x-1}\right)$
- $\displaystyle f(x) = \frac{1}{\sqrt{1-3x^4}}$
- $\displaystyle f(x) = x^2e^{-2x} + e^3$
:::

## 5.2 Composition of functions
The main thing about functions is that you can plug numbers into the function, and the function returns back some value. But, numbers aren't the only thing that can be plugged-into functions.

:::{caution} Example
:icon:false
Let $f(x) = 3x-1$ and $g(x) = x^2 + 5.$ Then
\begin{equation*}
\begin{split}
f(g(x)) &= f(x^2+5) \\ &= 3 \cdot (x^2+5) -1 \\ &= 3x^2 + 14 
\end{split}
\end{equation*}
Similarly,
\begin{equation*}
\begin{split}
g(f(x)) &= g(3x-1) \\ &= (3x-1)^2 + 5 \\ &= 9x^2-6x+6
\end{split}
\end{equation*}
:::

## 5.3 Limit of a function