# 4. Systems of linear equations

## 4.1 Introduction
When we were learning about the determinant of a matrix, we learned how to solve Cramer's systems. Cramer's system is a very special kind of a system because its matrix of coefficients $A$ is invertible. In this chapter, we are going to learn how to solve general systems of linear equations.

First, notice that not all systems of linear equations have a solution.
:::{caution} Example
:icon:false
The system of linear equations given by 
\begin{equation*} 
\begin{cases} x+y = 1 \\ x + y = 2 \end{cases} 
\end{equation*} 
obviously doesn't have a solution since $1$ cannot be equal to $2$.
:::
Therefore, we need to answer to questions:
- When does a given system of linear equations have a solution?
- If the given system has a solution, how do we compute it?

## 4.2 Kronecker-Capelli theorem
The following theorem gives us a way of checking if the given system of linear equations does have or does not have a solution.

:::{danger} Theorem (Kronecker - Capelli)
:icon:false
System of linear equations $AX = B$ has at least one solution if and only if 
\begin{equation*}
r(A) = r(A|B).
\end{equation*}
:::

:::{note} Problem 4.1
:icon:false
Check whether or not the following system of linear equations has a solution:
\begin{equation*}
\begin{cases}
x+2y+z = 4 \\ 2x+y+2z = 5 \\ 3x+2y+3z = 12
\end{cases}
\end{equation*}
:::

:::{note} Problem 4.2
:icon:false
Check whether or not the following system of linear equations has a solution:
\begin{equation*}
\begin{cases}
x+2y+3z = 1 \\ -x+3y-21z = 2 \\ 3x+7y+3z = 3
\end{cases}
\end{equation*}
:::

## 4.3 Gauss-Jordan method
Now that we know how to check whether or not a given system of linear equations has a solution, we want to know how to explicity compute the solutions (if they exist).

:::{note} Problem 4.3
:icon:false
Using the Gauss-Jordan algorithm, solve the system
\begin{equation*}
\begin{cases}
-2x+y+3z = 1 \\
x+2z = 1 \\
4x-y+5z = 1
\end{cases}
\end{equation*}
:::

:::{note} Problem 4.4
:icon:false
Using the Gauss-Jordan algorithm, solve the system
\begin{equation*}
\begin{cases}
2x+y = 3 \\
3x+5y = 8 \\
5x+6y = 11
\end{cases}
\end{equation*}
:::

:::{note} Problem 4.5
:icon:false
Using Gauss-Jordan algorithm, solve the system
\begin{equation*}
\begin{cases}
x+3y = 2 \\
2x+3y+3z = 7 \\
2x+z = 6 \\
3x+9y+3z = 12
\end{cases}
\end{equation*}
:::

:::{note} Problem 4.6
:icon:false
Using Gauss-Jordan algorithm, solve the following systems:
\begin{equation*} 
\begin{cases}
x+y-z = 0 \\ 2x-y+z = 0
\end{cases}
\end{equation*}
:::

## 4.4 Input-output model