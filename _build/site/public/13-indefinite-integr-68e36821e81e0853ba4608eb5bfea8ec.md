# 13. Indefinite integrals

## <span class = "h2-num">13.1 </span><span class = "h2-text"> Introduction </span>
The central problem of this part of the course is the following: how to calculate the area under the graph of a function?

In order to give a full answer to this question, we need to understand the following two questions:
- why would we care about the area under a graph of a function?
- how to calculate the area under the graph of a function?

The following chart illustrates the way in which we will answer these questions.

````{mermaid}
:label: chart
flowchart LR
A -- why? --> D
A[area] -- how? --> B -- how? --> C
B[definite integrals]
C[indefinite integrals]
D[probability]
````

This entire chapter is devoted to the second question - what new tools do we need in order to be able to find the area under the graph of a function? The answer is given in the [chart above](#chart) - we need to know how to compute **<span style = "color: green"> indefinite integrals.</span>**

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon: false
:label: def_integral
Let $f(x)$ be a given function. **<span style = "color : green"> Indefinite integral</span>** of the function $f$ is any function $F(x)$ such that
\begin{equation*}
F'(x) = f(x).
\end{equation*}
The integral of the function $f$ is denoted by $\displaystyle \int f(x) \, dx$.
:::
So, in some sense integration is the opposite operation of differentiation - given some function $f$, we want to find a function $F$ whose derivative is exactly the function $f$.

:::{prf:remark}
:numbered: false
Suppose that $F$ is an integral of the function $f$. [By definition](#def_integral), that means that
\begin{equation*}
F'(x) = f(x).
\end{equation*}
But also the following identities hold:
\begin{equation*}
\begin{split}
(F(x) + 2)' &= F'(x) + 2' = f(x) + 0 = f(x) \\
(F(x) + 17)' &= F'(x) + 17' = f(x) + 0 = f(x) \\
(F(x) + 1013)' &= F'(x) + 1013' = f(x) + 0 = f(x)
\end{split}
\end{equation*}
What we can see from this is that adding a constant to the integral of the function $f$ does not change the result, since the derivative of a constant is equal to zero. This is indicated by "$+C$" that you will see in the formulas in the following section, where that "$+C$" simply means that we can add any constant to an integral without affecting the end result.
:::

## <span class = "h2-num">13.2 </span><span class = "h2-text"> Direct integration </span>

:::{danger} <span style = "color: red">Basic rules for integration</span>
:icon: false
:class: dropdown
\begin{equation*}
\begin{split}
\int f + g \, dx &= \int f \, dx + \int g \, dx \\
\int c \cdot f \, dx &= c \cdot \int f \, dx
\end{split}
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
As it was with the derivative, not all integrals we would like to know how to compute can be calculated using just the most basic [formulas for integration](#table-integrals), so we need a new method that will allow us to find integrals of more complicated functions. One such method is called **<span style = "color : blue"> substitution method </span>.**

:::{prf:remark}
:numbered: false
Broadly speaking, there are three very common parts of functions that we often simplify by supstitution:
- denominators
- expressions under a root
- exponents
:::

:::{note} Problem 13.5
:icon: false
:label: P135
Calculate the integral $\displaystyle \int \frac{2x-2}{x^2-2x+9} \, dx.$
:::

````{solution} P135
:class: dropdown
We use the substitution methond in order to compute this integral:
\begin{equation*}
\begin{split}
\int \frac{2x-2}{x^2-2x+9} \, dx &= \left\{
    \begin{align*}
    t &= x^2 -2x + 9 \\
    dt &= (2x-2)dx \implies dx = \frac{dt}{2x-2}
    \end{align*}
    \right\} \\
&= \int \frac{2x-2}{t} \cdot \frac{dt}{2x-2} \\
&= \int \frac{1}{t} \, dt \\
&= \ln(t) \\
&= \ln(x^2-2x+9) + C.
\end{split}
\end{equation*}
````

:::{note} Problem 13.6
:icon: false
Calculate the integral $\displaystyle \int \frac{x}{\sqrt[3]{6x^2+6}} \, dx.$
:::

:::{note} Problem 13.7
:icon: false
Calculate the integral $\displaystyle \int x \cdot e^{3x^2 + 2} \, dx.$
:::

:::{note} Problem 13.8
:icon: false
:label: P138
Calculate the integral $\displaystyle \int \frac{1}{x \cdot \ln(x)} \, dx.$
:::

````{solution} P138
:class: dropdown
We use the substitution method in order to compute this integral:
\begin{equation*}
\begin{split}
\int \frac{1}{x \cdot \ln(x)} \, dx &= \left\{
    \begin{align*}
    t &= \ln(x) \\
    dt &= \frac{1}{x} \, dx \implies dx = x \cdot dt
    \end{align*}
    \right\} \\
&= \int \frac{1}{x \cdot t} \cdot x \, dt \\
&= \int \frac{1}{t} \, dt \\
&= \ln(t) \\
&= \ln(\ln(x)) + C.
\end{split}
\end{equation*}
````

:::{caution} 💡 
:icon:false
Notice the main point about substitution method: we get rid of the complicated part by using the substitution, and whatever is left afterwards is a straight-forward computation.
:::

## <span class = "h2-num">13.4 </span><span class = "h2-text"> Integration by parts </span>
As we will see in this section, not even relying solely on the substituion method will be enough to compute all the integrals we will need. Therefore, we are introducing yet another method of integration that we will use in order to find integrals - **<span style = "color : blue"> integration by parts. </span>** 

:::{danger} <span style = "color : red"> Integration by parts</span>
:icon: false
:label: formula_ibp
\begin{equation*}
\int u \, dv = u \cdot v - \int v \, du.
\end{equation*}
:::

:::{prf:remark}
:numbered: false
As you will see in the problems that follow, when using integration by parts you will have to choose which part of the integral is going to be equal to $u$, and which one is going to be equal to $dv$. Whatever you pick for $u$, you will have to differentiate and whatever you pick for $dv$, you will have to integrate. So, a general rule of thumb is to make such a choice so that integrating the differential $dv$ is easy.
:::

:::{note} Problem 13.9
:icon: false
:label: P139
Calculate the integral $\displaystyle \int (x+5) \cdot e^x \, dx.$
:::

````{solution} P139
:class: dropdown
We use the [formula for the integration by parts](#formula_ibp):
\begin{equation*}
\begin{split}
\int (x+5) \cdot e^{x} \, dx &= \left\{ 
    \begin{align*}
    u &= x+5 &\implies du &= dx \\
    dv &= e^x \, dx &\implies v&= \int dv = \int e^x \, dx = e^x
    \end{align*}
    \right\} \\
&= (x+5) \cdot e^x - \int e^{x} \, dx \\
&= (x+5) \cdot e^x - e^x + C.
\end{split}
\end{equation*}
Lastly, what would've happend if we reversed the roles of $u$ and $dv$ when applying the formula for integration by parts? Well, we would've got something more complicated than we started with - namely, the following:
\begin{equation*}
\begin{split}
\int (x+5) \cdot e^x \, dx &= \left\{
    \begin{align*}
    u &= e^x &\implies du &= e^x \, dx\\
    dv &= (x+5) \, dx &\implies v &= \int \, dv = \int (x+5) \, dx = \frac{1}{2} \cdot (x+5)^2
    \end{align*}
    \right\} \\
&= \frac{1}{2}(x+5)^2 \cdot e^x - \int \frac{1}{2}(x+5)^2 \cdot e^x \, dx.
\end{split}
\end{equation*}
Notice that with this choice we end up with having to calculate something more complicated than we originally had, so that's how you know whether or not you have made the correct choice when deciding what will be $u$ and what will be $dv$. Remember: the main point is get something simpler!
````


:::{note} Problem 13.10
:icon: false
Calculate the integral $\displaystyle \int x^3 \cdot \ln(x) \, dx.$
:::

:::{note} Problem 13.11
:icon: false
:label: P1311
Calculate the integral $\displaystyle \int \frac{x}{e^x} - 3x^2 \, dx.$
:::

````{solution} P1311
:class: dropdown
First of all, because the ingral of a sum is the sum of the integrals, we have
\begin{equation*}
\int \frac{x}{e^x} -3x^2 \, dx = \int \frac{x}{x^x} \, dx - \int 3x^2 \, dx.
\end{equation*}
So, in order to compute the integral in this question we simply need to compute the two integrals above. The second integral is easy, since we can use the formula given in the [table of integrals](#table-integrals):
\begin{equation*}
\int 3x^2 \, dx = x^3.
\end{equation*}
As for the first one, we use the integration by parts:
\begin{equation*}
\begin{split}
\int \frac{x}{e^x} \, dx &= \int x \cdot e^{-x} \, dx \\
&= \left\{ 
    \begin{align*}
    u &= x &\implies du &= dx\\
    dv &= e^{-x} \, dx &\implies v &= \int e^{-x} \, dx \, = -e^{-x}
    \end{align*}
    \right\} \\
&= -x \cdot e^{-x} - \int -e^{-x} \, dx \\
&= -x \cdot e^{-x} + \int e^{-x} \, dx \\
&= -x \cdot e^{-x} -e^{-x} + C
\end{split}
\end{equation*}
````

:::{caution} 💡 
:icon:false
In the same way as with subsitution method, we can use integration by parts to reduce the task of computing something rather complicated to computing something that is straight-forward.
:::

:::{prf:remark}
:numbered: false
When computing indefinite integrals, the first and the most important step is to know which of the three methods we need to use in order to compute the integral. To that end, the following simple chart illustrates the thought process that can be applied to figure that out:
```{mermaid}
flowchart TB
A[How to compute the given integral?] --> B
B[Can I write the function as a power of x?] -- yes  --> C
C[Use direct integration]
B -- no --> D
D[Would it be easier if I only had one variable
- a
- b
] -- yes --> E
E[Use substitution method]
```
:::