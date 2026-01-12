# 14. Definite integrals

## <span class = "h2-num">14.1 </span><span class = "h2-text"> Introduction </span>
As we mentioned at the beginning of the previous chapter, the main problem we are dealing with in this part of the course is regarding the area - how to find the area under the graph of a function?

Intuitively, the area under the graph of the function $f(x)$ can be found by approximating it rectangles.

:::{figure} ./video/Integral.mp4
How to use the rectangles to approximate the area under the graph of a function. In each iteration we are using rectangles of smaller and smaller width until they add up perfectly to the area we want to compute.
:::

Now that we have some intuitive understanding of how to compute the area, we want to know how can this be done mathematically. We have already done the first step in the previous chapter in which we learned how to compute indefinite integrals. The rest of the answer was also outlined in the previous chapter:
- learn how to find definite integrals
- use definite integrals to compute the area

## <span class = "h2-num">14.2 </span><span class = "h2-text"> Definite integrals </span>

In this section we are going to learn how to find definite integral of a given function $f(x)$, which will be denoted as $\displaystyle \int _a ^b f(x) \, dx$, where $a,b$ are just some numbers. The following formula tells us how to actually find definite integrals.

:::{danger} <span style = "color : red"> Theorem (Newton-Leibniz formula) </span>
:icon: false
The definite integral of the function $f(x)$ from $a$ to $b$ is equal to
\begin{equation*}
\int_a^b f(x) \, dx = F(b)-F(a),
\end{equation*}
where $\displaystyle F(x) = \int f(x) \, dx$.
:::

Therefore, we see that indeed we first need to know how to compute an indefinite integral of a function in order to be able to find its definite integral.

:::{note} Problem 14.1
:icon: false
Calculate the value of the integral $\displaystyle \int_1^3 3x^2 +2x \, dx.$
:::

:::{note} Problem 14.2
:icon: false
Calculate the value of the integral $\displaystyle \int_{-7}^{-5} \frac{2x}{x^2+1} \, dx.$
:::

:::{note} Problem 14.3
:icon: false
Calculate the value of the integral $\displaystyle \int_{1}^{10} \ln(x) \, dx.$
:::

:::{prf:remark}
:numbered: false
It is easy to recognize when we are dealing with an indefinite and when with a definite integral since the definite integrals have two numbers displayed that tell us from where to where are we integrating the given function.
:::

## <span class = "h2-num">14.3 </span><span class = "h2-text"> Area </span>
In this section we are going to use the definite integral to compute the area. Namely, the area under the graph of the function $f(x)$ over the segment $[a,b]$ is equal to the value of the definite integral $\displaystyle \int_a^b f(x) \, dx$.

:::{note} Problem 14.4
:icon: false
Find the area under the graph of the function $f(x) = x^2 + 5$ over the segment $[1,4]$.
:::

:::{note} Problem 14.5
:icon: false
Find the area limited by the graph of the function $f(x) = -x^2 +2x + 8$ and the $x$-axis.
:::

:::{note} Problem 14.6
:icon: false
Find the area limited by the graphs of the functions 
\begin{equation*}
f(x) = -x+ \frac{5}{2}, \quad g(x) = \frac{1}{x}.
\end{equation*}
:::

:::{note} Problem 14.7
:icon: false
Find the area limited by the graphs of the functions
\begin{equation*}
f(x) = 4, \quad g(x) = \frac{1}{x}, \quad h(x) = x^2.
\end{equation*}
:::