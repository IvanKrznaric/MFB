# 8. Optimization of functions of one variable

## <span class = "h2-num">8.1 </span><span class = "h2-text"> Introduction </span>
In this chapter, we are going to see how to use the derivative in order to answer the following questions:
- How to find local extrema, i.e. local minimums/maximums of a given function?
- How to find the intervals over which the given function is increasing/decreasing?
- How to find the intervals over which the given function is convex/concave?

The answers to all of these questions are going to be algorithmic in nature, meaning we will state the algorithm which will lead us to answers to the questions above. The main thing that we'll use to derive those algorithms is the relationship between the function $f$ and its derivatives.

:::{figure} ./video/Optimizacija.mp4
The relationship between the function $f$ and its derivatives.
:::

## <span class = "h2-num">8.2 </span><span class = "h2-text"> Local extrema </span>
:::{note} ⚙️ How to find the local extrema of a function $f$
:icon:false
1. Find the domain of the function $f$
2. Find the stationary points, i.e. solve the equation $f'(x) = 0$
3. Use the $2^{\text{nd}}$ derivative to determine which points are minimums and which are maximums.
:::

:::{note} Problem 8.1
:icon: false
Let $\displaystyle f(x) = e^x - x.$ Find the local extreme points and the corresponding extreme values.
:::

:::{figure} ./slike/LocEx
Graph of the function $f(x) = e^x -x.$ The point $x = 0$ is a local minimum of the function $f.$
:::

:::{note} Problem 8.2
:icon: false
Let $\displaystyle f(x) = \frac{x}{1+x^2}.$ Find the local extreme points and the corresponding extreme values.
:::

:::{note} Problem 8.3
:icon: false
Let $\displaystyle f(x) = \ln(1+x^4).$ Find the local extreme points and the corresponding extreme values.
:::

:::{note} Problem 8.4
:icon: false
Let $\displaystyle f(x) = \frac{x^2-2}{x} -3\ln(x).$ Find the local extreme points and the corresponding extreme values.
:::

:::{note} Problem 8.5
:icon: false
Let $\displaystyle f(x) = (x+2x^2)e^{-x}.$ Find the local extreme points and the corresponding extreme values.
:::

## <span class = "h2-num">8.3 </span><span class = "h2-text"> Intervals of monotonicity </span>

:::{note} ⚙️ How to find intervals of monotonicity of a function $f$
:icon:false
1. Find the domain of the function $f$
2. Find the stationary points, i.e. solve the equation $f'(x) = 0$
3. Make the table of the signs of the $1^{\text{st}}$ derivative $f'$ and read off the intervals.
:::

:::{note} Problem 8.6
:icon: false
Find the intervals over which the function $\displaystyle f(x) = \frac{x^2}{4-x} $ is increasing and decreasing.
:::

:::{figure} ./slike/IntMon.png
Graph of the function $\displaystyle f(x) = \frac{x^2}{4-x}.$
:::

:::{note} Problem 8.7
:icon: false
Find the intervals over which the function $\displaystyle f(x) = \frac{1-\sqrt{x}}{1+\sqrt{x}}$ is increasing and decreasing.
:::

:::{note} Problem 8.8
:icon: false
Find the intervals over which the function $\displaystyle f(x) = (2x^2+x)e^{-x}$ is increasing and decreasing.
:::

:::{note} Problem 8.9
:icon: false
Find the intervals over which the function 
\begin{equation*}
f(x) = e^{-x}(x^2+1) + \frac{(x-1)^3}{3}
\end{equation*}
 is increasing and decreasing.
:::

:::{error} Common mistake on the Midterm/Exam
:class: dropdown
A common mistake that students make when they are asked to define an increasing function is that they say that a function is increasing **if** $f'(x) > 0.$ That statement is **<span style = "color:red"> not correct! </span>** \
By definition, a function is increasing if 
\begin{equation*}
x < y \implies f(x) < f(y)
\end{equation*}
Of course, if a function $f$ is increasing, then $f'(x) > 0,$ but having a positive derivative is not the definition of an increasing function, but rather a consequence of the definition. \
Keep in mind what is defining property of something, and what is a consequence of the definition!
:::

## <span class = "h2-num">8.4 </span><span class = "h2-text"> Convexity and concavity </span>

:::{note} ⚙️ How to find intervals of convexity of a function $f$
:icon:false
1. Find the domain of the function $f$
2. Find the $2^{\text{nd}}$ derivative $f''(x)$ and solve the equation $f''(x) = 0$
3. Make the table and read off the intervals.
:::

:::{note} Problem 8.10
:icon: false
Find the intervals over which the function $\displaystyle f(x) = x^3-4x$ is convex and concave.
:::

:::{figure} ./slike/Conv.png
Graph of the function $\displaystyle f(x) = x^3-4x.$ 
:::

:::{note} Problem 8.11
:icon: false
Find the intervals over which the function $\displaystyle f(x) = \frac{\ln(x)}{x}$ is convex and concave.
:::

:::{note} Problem 8.12
:icon: false
Find the intervals over which the function $\displaystyle f(x) = e^{-x}(1+x^2)$ is convex and concave.
:::

:::{note} Problem 8.13
:icon: false
Find the intervals over which the function $\displaystyle f(x) = (x+1)\ln(x+1)$ is convex and concave.
:::