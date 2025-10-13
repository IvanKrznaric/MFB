# 3. Rank of a matrix

## 3.1 Introduction

## 3.2 Vectors
:::{tip} Definition
:icon:false
Let $a_1, \dots, a_k \in \R^n$ be vectors with $n$ components and let $c_1, \dots, c_k \in R$ be real numbers. The vector
\begin{equation*} c_1a_1 + \dots + c_k ak\end{equation*}
is called **a linear combination** of vectors $a_1, \dots, a_k.$
:::

```{exercise}
:enumerator: 3.1
Let $a_1 = \begin{bmatrix} 1 & 1 & 0\end{bmatrix}, a_2 = \begin{bmatrix} 5 & -2 & 3 \end{bmatrix}, a_3 = \begin{bmatrix} -1 & 0 & 0 \end{bmatrix}.$ Find the linear combination of these vectors given by $v = -3a_1+2a_2-a_3.$
```

:::{tip} Definition
:icon:false
The vectors $a_1, \dots, a_k$ are said to be **linearly independent** if 
\begin{equation*}c_1a_1 + c_2a_2 + \dots + c_k a_k = 0 \implies c_1 = c_2 = \dots = c_k = 0 \end{equation*}
Otherwise, we say that these vectors are **linearly dependent**.
:::

```{exercise}
:enumerator: 3.2
Check if the following vectors are linearly dependent or independent:
\begin{equation*} a_1 = \begin{bmatrix}  1 & 1 & 0 \end{bmatrix}, \quad a_2 = \begin{bmatrix} 1 & 2 & 0 \end{bmatrix}, \quad a_3 = \begin{bmatrix} 2 & 0 & 1 \end{bmatrix}. \end{equation*}
```

## 3.3 Rank of a matrix
As we have seen, checking whether or not the given vectors are linearly dependent or independent using the definition can be quite messy - it boils down to solving systems of equations. So, we would like to come up with an easier method of checking the linear (in)dependence of vectors.

:::{tip} Definition
:icon:false
**The rank** of the matrix $A$ is the maximum number of its linearly independent columns. That number is denoted by $r(A).$
:::

:::{exercise}
:enumerator: 3.3
Find the rank of the matrix $A = \begin{bmatrix} 1 & 5 \\ 0 & 1 \end{bmatrix}.$
:::

:::{exercise}
:enumerator: 3.4
Find the rank of the matrix $A = \begin{bmatrix} 1 & 1 & -2 \\ 0 & 1 & -2 \\ 0 & 0 & 4\end{bmatrix}.$
:::

:::{exercise}
:enumerator: 3.5
Find the rank of the matrix $A = \begin{bmatrix} 1 & 1 & -2 \\ 0 & 1 & -2 \\ 0 & 0 & 0\end{bmatrix}.$
:::

:::{exercise}
:enumerator: 3.6
Find the rank of the matrix $A = \begin{bmatrix} 1 & 2 & 3 & 6 \\ 0 & 5 & 6 & 11 \\ 0 & 0 & 8 & 8 \\ 0 & 0 & 0 & 0\end{bmatrix}.$
:::

:::{exercise}
:enumerator: 3.7
Find the rank of the matrix $A = \begin{bmatrix}1 & 0 & 2 & 1 \\ 0 & 1 & -3 & 1 \\ 0 & 0 & 1 & 0 \end{bmatrix}.$
:::

:::{note} ⚙️ Gauss-Jordan algorithm
:icon:false
1. Choose an element in the first column that you can use to cancel out all other elements in the first column
2. Interchange the corresponding rows so that the chosen element is in the position $(1,1)$
3. Cancel out the elements underneath the chosen element
4. Forget about the first row and first column
5. Repeat
:::

```{exercise}
:enumerator: 3.8
Find the rank of the matrix $A = \begin{bmatrix} 2 & 1 & 1 & 0 \\ 1 & 2 & -1 & -3 \\ 0 & 1 & -1 & -3 \\ 1 & 3 & -2 & -5 \end{bmatrix}.$
```

:::{caution} 💡
:icon: false
:::