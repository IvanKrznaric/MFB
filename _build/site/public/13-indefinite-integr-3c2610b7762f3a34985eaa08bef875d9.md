# 13. Indefinite integrals

## <span class = "h2-num">13.1 </span><span class = "h2-text"> Introduction </span>

## <span class = "h2-num">13.2 </span><span class = "h2-text"> Direct integration </span>

:::{danger} <span style = "color: red">Basic rules for integration</span>
:icon: false
:class: dropdown
\begin{equation*}
\int f + g \, dx = \int f \, dx + \int g \, dx \quad \quad \int c \cdot f \, dx = c \cdot \int f \, dx
\end{equation*}
:::

:::{danger} <span style = "color : red"> Table of integrals</span>
:icon: false
:label: table-integrals
:class: dropdown
\begin{equation*}
\begin{split}
\int c \, dx &= cx + C, \quad \quad \int x^n \, dx = \frac{1}{n+1}\cdot x^{n+1} + C \\
\int a^x \, dx &= \frac{1}{\ln(a)}\cdot a^x + C, \quad \quad \int e^x \, dx = e^x + C, \quad \quad \int \frac{1}{x} \, dx = \ln(x) + C
\end{split}
\end{equation*}
:::

:::{note} Problem 13.1
:icon: false
Calculate the integral $\displaystyle \int x^3 - 5x^4 + x -1 \, dx.$
:::

:::{note} Problem 13.2
:icon: false
Calculate the integral $\displaystyle \int x \cdot \sqrt[3]{x} - \frac{x^5}{\sqrt{x}} \, dx.$
:::

:::{note} Problem 13.3
:icon: false
Calculate the integral $\displaystyle \int 4^x \cdot 5^{-x} \, dx.$
:::

:::{note} Problem 13.4
:icon: false
Calculate the integral $\displaystyle \int \frac{x^2 + 1}{x} \, dx.$
:::

## <span class = "h2-num">13.3 </span><span class = "h2-text"> Substitution method </span>
As it was with the derivative, not all integrals we would like to know how to compute can be calculated using just the most basic [formulas for integral](#table-integrals), so we need a new method that will allow us to find integrals of more complicated functions. One such method is called **<span style = "color : blue"> substitution method </span>.**

:::{note} Problem 13.5
:icon: false
Calculate the integral $\displaystyle \int \frac{2x-2}{x^2-2x+9} \, dx.$
:::

:::{note} Problem 13.6
:icon: false
Calculate the integral $\displaystyle \int \frac{x}{\sqrt[3]{6x^2+6}} \, dx.$
:::

## <span class = "h2-num">13.4 </span><span class = "h2-text"> Integration by parts </span>
