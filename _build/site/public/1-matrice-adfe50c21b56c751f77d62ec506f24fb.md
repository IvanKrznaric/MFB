# 1. Matrices and matrix operations

## 1.1 Introduction

:::{prf:example}
:numbered:false
A certain economy is comprised of the following three sectors: agriculture, manufacturing and energy. Each industry consumes a percentage of outputs from the other industries in order to produce its goods, and those percentages are given in the following table:
:::

:::{prf:definition}
:numbered:false
**A matrix** is a rectangular array of numbers. If a matrix has $n$ rows and $m$ columns, we say that the **order** of that matrix is $n \times m.$
:::
There are two ways in which we can specifiy a matrix:
- you can write it down explicitly
- we can specify its order and state the formula for computing its entries


```{exercise}
:enumerator:1.1
Consider the matrix $M = \begin{bmatrix} 1 & 0 & 2 \\ e & \pi & \frac{1}{7} \end{bmatrix}.$
1. What is the order of this matrix?
2. Which element is at the position $(2,1)$ and which is at the position $(1,2)$?
```

```{exercise}
:enumerator: 1.2
Write out a matrix $B = [b_{ij}]$ of order $3 \times 4$ such that $b_{ij} = i^2 - j^2.$
```

## 1.2 Types of matrices
:::{prf:definition}
:numbered:false
A matrix that has the same number of rows and columns is called a **square matrix.** Otherwise, a matrix is called **rectangular matrix.**
:::

:::{prf:definition}
:numbered:false
A square matrix is called
- **diagonal matrix** if all its elements outside the main diagonal are equal to $0$
- **scalar matrix** if it is a diagonal matrix whose entries on the main diagonal are equal
:::

```{exercise}
:enumerator: 1.3
What do we call the following matrices:
:::{math}
:enumerated:false
\begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \end{bmatrix}, \quad \begin{bmatrix} - \sqrt[3]{2} & 0 & 0 \\ 0 & - \sqrt[3]{2} & 0 \\ 0 & 0 & -\sqrt[3]{2} \end{bmatrix}?
:::
```

## 1.3 Matrix operations