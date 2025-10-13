# 3. Rank of a matrix

## 3.1 Introduction

## 3.2 Vectors
:::{prf:definition}
:numbered:false
Let $a_1, \dots, a_k \in \R^n$ be vectors with $n$ components and let $c_1, \dots, c_k \in R$ be real numbers. The vector
\begin{equation*} c_1a_1 + \dots + c_k ak\end{equation*}
is called **a linear combination** of vectors $a_1, \dots, a_k.$
:::

```{exercise}
:enumerator: 3.1
Let $a_1 = \begin{bmatrix} 1 & 1 & 0\end{bmatrix}, a_2 = \begin{bmatrix} 5 & -2 & 3 \end{bmatrix}, a_3 = \begin{bmatrix} -1 & 0 & 0 \end{bmatrix}.$ Find the linear combination of these vectors given by $v = -3a_1+2a_2-a_3.$
```

:::{prf:definition}
:numbered:false
The vectors $a_1, \dots, a_k$ are said to be **linearly independent** if 
\begin{equation*}c_1a_1 + c_2a_2 + \dots + c_k a_k = 0 \implies c_1 = c_2 = \dots = c_k = 0 \end{equation*}
:::