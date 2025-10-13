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

:::{tip} Definition
:icon:false
Let $A$ be a $n \times n$ matrix. We say that a $n \times n$ matrix $X$ is **the inverse** of the matrix $A$ if 
\begin{equation*} A \cdot X = X \cdot A = I .\end{equation*}
In that case, we say that the matrix $A$ is **invertible** or **regular**. The inverse $X$ of the matrix $A$ is denoted by $A^{-1}.$
:::

:::{note}
Of course, the inverse of the matrix $A$ is denoted by $A^{-1}$ for the same reason why the reciprocal value of the number $7$ is denoted by $7^{-1}.$
:::

So, if we would like to divide the matrix $A$ by the matrix $B$, we would need to find the inverse $B^{-1}$ of the matrix $B$ and then compute $A \cdot B^{-1}.$ However, here we stumble upon a problem - not all matrices are invertible.

:::{note} Problem 2.1
:icon:false
Show that the matrix $A = \begin{bmatrix} 1 & 1 \\ 1 & 1\end{bmatrix}$ isn't invertible, i.e. it does not have an inverse.
:::

## 2.2 Determinant of a matrix
Because not every matrix is invertible, we need a criterion that will allow us to check whether or not a given matrix has an inverse. For that, we will be using *the determinant*. **The determinant** is a number that is associated to every square matrix. The determinant of a matrix $A$ is denoted by $\lvert A \rvert$ or by $\text{det}(A).$ The determinant of a $2 \times 2$ matrix is given by a simple formula 
:::{math}
:numbered:false
\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc.
:::

:::{note} Problem 2.2
:icon:false
Find the determinant of the matrix $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}.$
:::

In order to find determinant of matrices of higher order, we will use two methods:
- Laplace expansion
- Elementary transformations

:::{note}
Although you can use each method separately, in most of the problems it will be best if you use both of them together to find the determinant.
:::

### Laplace expansion

:::{note} ⚙️ Laplace expansion
:icon:false
1. Choose a row or a column (preferably one with the most zeros)
2. Determine the signs of its elements
3. Run through the chosen row/column and expand
:::

:::{note} Problem 2.3
:icon:false
Find the determinant of the matrix $A = \begin{bmatrix} 1 & 0 & 0 & 4 \\ 2 & 3 & 4 & 1 \\ 3 & 0 & 1 & 0 \\ 4 & 1 & 2 & 3 \end{bmatrix}.$
:::

:::{caution} 💡 
:icon:false
Notice the main point about Laplace expansion: with each application of a Laplace expansion, we are reducing the order of the matrix whose determinant we need to calculate and hence we are reducing the complexity of our calculations.
:::

:::{note} Problem 2.4
:icon:false
Find the determinant of the following matrices:
\begin{equation*} A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 3 & 1 \\ 0 & 0 & 2 \end{bmatrix}, \quad B = \begin{bmatrix} 2 & 0 & 0 \\ 3 & 3 & 0 \\ 2 & 2 & 2 \end{bmatrix}.\end{equation*}
:::

:::{note} Problem 2.5
:icon:false
Find the determinant of the matrix $A = \begin{bmatrix} 2 & -4 & 8 & 11 \\ -5 & 7 & -3 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 27 & -33 & 4 \end{bmatrix}.$
:::




### Elementary transformations
As we have seen, Laplace expansion is a very useful method of finding the determinant of a matrix that has a lot of zeros along some row or a column, however what if our has matrix doesn't have any zeros? In that case, we will use **elementary transformations** to get the zeros in our matrix so that we can use the Laplace expansion to find the determinant. To use an elementary transformation simply means to multiply a row of a matrix by some number and adding it to some other row. Obviously, the end-goal of performing elementary transformations is to get zeros along some column of the given matrix so that we can use Laplace expansion to calculate the determinant. 

:::{note} Problem 2.6
:icon:false
Find the determinant of the matrix $A = \begin{bmatrix} 2 & 1 & 4 \\ 4 & 2 & 9 \\ 8 & 4 & 17 \end{bmatrix}.$
:::

:::{note} Problem 2.7
:icon:false
:label: transponiranje
Let $A = \begin{bmatrix} 1 & -6 & -1 \\ -2 & 1 & 2 \\ 3 & 0 & 1 \end{bmatrix}.$
- find the determinant of the matrix $A$
- find the determinant of the transpose $A^T$ of the matrix $A$
:::

:::{note}
Notice that in the [](#transponiranje) we got that $\text{det}(A^T) = \text{det}(A).$ That formula holds for all square matrices so once we find $\text{det}(A)$ we immediately know what is $\text{det}(A^T)$ equal to.
:::

:::{caution} 💡
:icon:false
Notice the main point of elementary transformations: when a matrix has a lot of zeros, finding the determinant is easy because we can use the Laplace expansion. If the matrix doesn't have a lot of zeros, we are using elementary transformations to reduce the complexity of the matrix and to obtain something very simple that we know how to work with.
:::

The most important theorem when talking about the determinant is the **Binet-Cauchy theorem**.

:::{danger} Theorem (Binet-Cauchy)
:icon:false
Let $A,B$ be two $n \times n$ matrices. Then $\text{det}(A \cdot B) = \text{det}(A) \cdot \text{det}(B).$
:::

```{exercise}
:enumerator: 2.8
Let $A = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 2 & 4 \\ 0 & 0 & 1 \end{bmatrix}$ and $B = \begin{bmatrix} 2 & 8 & 16 \\ 0 & 1 & 2 \\ 0 & 0 & 2 \end{bmatrix}.$ \
If $X$ is a $3 \times 3$ matrix such that $XA = B,$ find the determinant of the matrix $X$.
```
## 2.3. Matrix inversion
As we have mentioned in the introduction, the main point of the determinant is to give us a criterion for checking whether or not a matrix has an inverse or not. That criterion is the following:

:::{prf:criterion}
:numbered:false
\begin{equation*} 
\begin{split}
\text{det}(A) \neq 0 &\implies A \text{ has an inverse} \\ 
\text{det}(A) = 0 &\implies A \text{ doesn't have an inverse}
\end{split}
\end{equation*}
:::

Next thing we would like to know is how to explicitly compute the inverse of a matrix. 

:::{prf:definition}
:numbered:false
Let $A = [a_{ij}] \in M_n$ be a square matrix. 
- **The minor** of an element $a_{ij}$ is the determinant of a matrix obtained by deleting the $i$-th row and the $j$-th column of the matrix $A$. That number is denoted by $M_{ij}$.
- **The cofactor matrix** is a $n \times n$ matrix $C = [c_{ij}],$ where 
\begin{equation*} c_{ij} = (-1)^{i+j}M_{ij} \end{equation*} 
- **The adjoint** of the matrix $A$ is the matrix $A^{\ast} = C^T.$
:::
Finally, the inverse of the matrix $A$ is given by the formula 
\begin{equation*} A^{-1} = \frac{1}{\text{det}(A)}A^\ast.\end{equation*}

```{exercise}
:enumerator: 2.9
Let $A = \begin{bmatrix} 2 & 4 & 1 \\ 4 & 3 & 7 \\ 2 & 1 & 3\end{bmatrix}.$
- Show that the matrix $A$ is invertible;
- Using the adjoint, find the inverse $A^{-1}$ of the matrix $A$
```

## 2.4 Cramer's systems
One of the main application of matrices we are going to see is revolving around solving system's of linear equations.
:::{prf:example}
:numbered: false
The system
\begin{equation*} \begin{cases} 2x-5y = 15 \\ 3x+y = 31. \end{cases} \end{equation*}
can be written in the matrix form as 
\begin{equation*} \begin{bmatrix} 2 & -5 \\ 3 & 1 \end{bmatrix} \cdot \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 15 \\ 31 \end{bmatrix} \end{equation*}
:::

In general, every system can be written in matrix form as 
\begin{equation*} AX = B, \end{equation*}
where $A$ is **the matrix of coefficients**, $X$ is the column-matrix of unknowns and $B$ is the column-matrix of the right-hand side of the system.

:::{prf:definition}
:numbered: false
We say that a system $AX = B$ of $n$ equations with $n$ unknows is **Cramer's system** if $\text{det}(A) \neq 0.$
:::

Cramer's system are particularly easy to solve because their solutions are given by the formula
\begin{equation*} x_i = \frac{D_i}{D}, \quad i = 1, \dots, n\end{equation*}
where $D = \text{det}(A)$ and $D_i$ is the determinant of the matrix obtained by replacing the $i$-th column of the matrix $A$ by the column-matrix $B$.

```{exercise}
:enumerator: 2.10
By using Cramer's rule, solve the following system of linear equations:
\begin{equation*} \begin{cases} x_1 -6x_2 -x_3 = -6 \\ -2x_1 + x_2 +2x_3 = 1 \\ 3x_1 +x_3 = 4 \end{cases} \end{equation*}
```