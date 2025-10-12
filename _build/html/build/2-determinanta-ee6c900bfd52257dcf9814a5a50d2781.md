# 2. Determinant of a matrix

## 2.1 Introduction
In the previous chapter we learned that matrices are very similar to numbers - you know how to add two matrices, how to subtract them and you know how to multiply two matrices. The only operation we haven't mentioned so far is divison - if you have two matrices $A$ and $B$, what would it mean to divide matrix $A$ by the matrix $B$?

In order to answer that quesion, let's see what does it mean to divide two numbers: for example, if we are given numbers $5$ and $7$, then to divide number $5$ by $7$ we have to multiply $5$ by $\frac{1}{7},$ i.e.
:::{math}
:numbered:false
5 \div 7 = 5 \cdot \frac{1}{7}.
:::
What is the connection between numbers $7$ and $\frac{1}{7}?$ Well, if we multiply them in any order, we get number $1$ as a result:
:::{math}
:numbered:false
7 \cdot \frac{1}{7} = \frac{1}{7} \cdot 7 = 1
:::
This also means that **the reciprocal value** or **the inverse** of the number $7$ is $\frac{1}{7}.$

So, we can see that there are two parts that are crucial when dividing number $a$ by the number $b$:
1. Find the inverse $\frac{1}{b}$ of the number $b$
2. Multiply $a$ and $\frac{1}{b}$

We can use this approach to define "divison" of matrices. If we would like to divide matrix $A$ by the matrix $B$, firstly we need to define what would be the *inverse* of the matrix $B$ and then we would simply need to multiply $A$ by that inverse.

:::{prf:definition}
:numbered:false
Let $A$ be a $n \times n$ matrix. We say that a $n \times n$ matrix $X$ is **the inverse** of the matrix $A$ if 
\begin{equation*} A \cdot X = X \cdot A = I .\end{equation*}
In that case, we say that the matrix $A$ is **invertible** or **regular**. The inverse $X$ of the matrix $A$ is denoted by $A^{-1}.$
:::

:::{prf:remark}
:numbered:false
Of course, the inverse of the matrix $A$ is denoted by $A^{-1}$ for the same reason why the reciprocal value of the number $7$ is denoted by $7^{-1}.$
:::