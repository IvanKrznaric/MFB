## 1. Matrices and matrix operations

### 1.1 Introduction

:::{prf:example} 
A certain economy is comprised of the following three sectors: 
:::

:::{prf:definition}
**A matrix** is a rectangular array of numbers. If a matrix has $n$ rows and $m$ columns, we say that **the order** of that matrix is $n \times m.$
:::

```{exercise}
:label: my-exercise

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```