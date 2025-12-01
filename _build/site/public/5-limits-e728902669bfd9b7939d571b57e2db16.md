# 5. Domains and limits of functions

## <span class = "h2-num">5.1 </span><span class = "h2-text"> Domain of a function </span>

:::{tip} <span style = "color : #228B22"> Definition </span>
:icon:false
**<span style = "color:green"> Domain </span>** of the function $f$ is the set of all real numbers $x$ for which that function is defined. Such as set is denoted by $\mathcal{D}_f.$
:::

:::{note} Problem 5.1
:icon:false
Find the domains of the following functions:
\begin{equation*}
\begin{split}
&a) \hspace{0.1 cm} f(x) = 3x^2-5x+9, \quad b) \hspace{0.1 cm} g(x) = \sqrt{x+9}, \quad c) \hspace{0.1 cm} h(x) = \sqrt[3]{x+7}, \\
& \hspace{0.2 cm} \\
& d) \hspace{0.1 cm} u(x) = \frac{-2x^2+x+1}{x^2+x-6}, \quad e) \hspace{0.1 cm} v(x) = \ln(x-3)
\end{split}
\end{equation*}
:::

:::{note} Problem 5.2
:icon:false
Find the domains of the following functions:
\begin{equation*}
f(x) = \ln \left( \frac{x+1}{x-1} \right), \quad g(x) = \frac{1}{\sqrt{2-3x^4}}, \quad h(x) = x^2 e^{-2x} +e^3.
\end{equation*}
:::


## <span class = "h2-num">5.2 </span><span class = "h2-text"> Composition of functions </span>
The main thing about functions is that you can plug numbers into the function, and the function returns back some value. But, numbers aren't the only thing that can be plugged-into functions.

:::{caution} <span style = "color:#8B4000"> Example </span>
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

The operation of pluggin-in one function inside another is called **<span style = "color:green"> composition of functions. </span>** When we are trying to recognize whether or not a given function is a composition of two or more functions, we are always moving from the "outside" to the "inside", where the "outside" function is, generally speaking, the one that appears first.

:::{note} Problem 5.3
:icon: false
Let $f(x) = \sqrt[3]{x}$ and $g(x) = 2x^2 -13x + 17.$ Compute the compositions $f(g(x))$ and $g(f(x)).$
:::

:::{note} Problem 5.4
:icon:false
Consider the following compositions:
- $\displaystyle F(x) = \sqrt{5x^2-4x}$
- $\displaystyle G(x) = e^{\sqrt[5]{x}}$
- $\displaystyle H(x) = \ln(x^2+1)$

For each composition determine which function is the "outside" function and which one is the "inside" function.
:::

## <span class = "h2-num">5.3 </span><span class = "h2-text"> Limit of a function </span>

Intuitively, **<span style = "color:green"> the limit </span>** of a function represents the "limiting" value of a function as the independent variable $x$ approaches a certain value, or gets arbitrarily large or small.

The main reason why we are studying limits of functions is so that we can understand the definition of the *derivative* of a function that we are going to be covering in the next chapter.

:::{note} Problem 5.5
:icon:false
Find the limit $\displaystyle \lim_{x \to \infty} \frac{2}{x}.$
:::

:::{figure} ./video/Limes1.mp4
As $x$ gets arbitrarily large, the value of the function $\frac{2}{x}$ get closer and closer to $0$ - hence, the limit is $0.$
:::

:::{note} Problem 5.6
:icon:false
Find the limit $\displaystyle \lim_{x \to \infty} \frac{1}{\sqrt{x}}.$
:::

:::{figure} ./video/Limes2.mp4
As $x$ gets arbitrarily large, the value of the function $\frac{1}{\sqrt{x}}$ gets closer and closer to $0$ - hence, the limit is $0.$
:::

In the previous problems, we could find the value of the limit by simply "plugging-in" the value $x$ approaches into the function. In the following problems, if we "plug-in" the value $x$ is approaching, we will get one of the following expressions:
\begin{equation*}
\frac{\infty}{\infty}, \quad \infty - \infty, \quad \frac{0}{0}.
\end{equation*}
In these cases, we need to simplify the expression we are dealing with in order to find the limit.

:::{note} Problem 5.7
:icon:false
Find the limit $\displaystyle \lim_{x \to \infty} \frac{2x^2+x+1}{2x^2+3}.$
:::

:::{note} Problem 5.8
:icon:false
Find the limit $\displaystyle \lim_{x \to \infty} \sqrt{x} (\sqrt{x+1}-\sqrt{x}).$
:::

:::{note} Problem 5.9
:icon: false
Find the limit $\displaystyle \lim_{x \to 1} \frac{2x^2-6x+4}{3x^2-12x+9}.$
:::

In the following problem, we are going to use the following formula:
\begin{equation*}
\lim_{x \to \infty} \left(1+ \frac{r}{x} \right)^{x} = e^r, \quad r \in \mathbb{R}
\end{equation*}

Notice that, if $r = 1$ then the formula above gives us
\begin{equation*}
\lim_{x \to \infty}\left(1+\frac{1}{x} \right)^{x} = e,
\end{equation*}
where $e$ is the Euler's number $e = 2.7182818284590\dots$

:::{figure} ./video/Limes_e.mp4
As $x$ gets arbitrarily large, the value of the function $\left(1+\frac{1}{x}\right)^x$ gets closer and closer to $e.$
:::

:::{attention} <span style = "color:#8B4000"> Euler's number and compound interest </span>
Imagine that you deposited $p$ euros into a bank and let's suppose that the bank will offer you an annual interest rate that's equal to $r$ (for example, $r = 0.1$ means that the annual interest rate is $10$ percent). We are interested in the value $a$ our initial deposit will have after the interest has been paid out. 

If the interest is paid out once a year, then at the end of the year our initial deposit will be worth
\begin{equation*}
a = p(1+r).
\end{equation*}

If the interest is paid out twice a year, then our initial deposit will be worth:
\begin{equation*}
\begin{split}
\text{after six months: } &a = p\left(1+\frac{r}{2}\right). \\
\text{at the end of the year: } &a = p\left(1+\frac{r}{2}\right) \cdot \left(1+\frac{r}{2}\right) = p\left(1+\frac{r}{2}\right)^2.
\end{split}
\end{equation*}
Generalizing, if the interest is paid out $x$ times a year, then at the end of the year our initial deposit will be worth
\begin{equation*}
a = p\left(1+\frac{r}{x}\right)^x.
\end{equation*}
If the interest is being paid-out in very small time intervals - meaning quite a lot of times during a year - then $x$ is a very very big number and we can find the value of the initial deposit at the end of the year by using the formula stated above:
\begin{equation*}
a = \lim_{x \to \infty} p \left(1+\frac{r}{x}\right)^x = p \cdot \lim_{x \to \infty} \left(1+\frac{r}{x}\right)^x = p \cdot e^r.
\end{equation*}
:::

:::{note} Problem 5.10
:icon:false
Find the limit $\displaystyle \lim_{x \to \infty} \left(\frac{x+2}{x}\right)^{7x}.$
:::