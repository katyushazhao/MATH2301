# MATH2301 Assignment 4
## (1) Consider a graph whose adjacency matrix is $A=\begin{pmatrix}1&1&1\\0&1&1\\0&0&1\end{pmatrix}$. Find the number of paths of length $4$ from $1$ to $3$
$A^2=\begin{pmatrix}1&2&3\\0&1&2\\0&0&1\end{pmatrix}$\
$A^4=\begin{pmatrix}1&4&10\\0
&1&4\\0&0&1\end{pmatrix}$\
Since $A^4_{1,3}=10$ there are $10$ paths of length $4$ from $1$ to $3$.

<div style="page-break-after: always;"></div>

## (2)
### (a) Find (without explicit calculation) an example of a $4\times4$ nonzero adjacency matrix such that all powers beyond the 10th power are 0. Justify briefly.
$\begin{pmatrix}0&1&1&1\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix}$\
The matrix is connected only one way so there are no paths with length more than $1$.

<div style="page-break-after: always;"></div>

### (b) Is it true that the 8th power of any such matrix (not just your example!) must also be zero?
A graph with $4$ nodes will either loop indefinitely or have a max path of $3$. So a $4\times4$ adjacency matrix where all powers beyond the 10th power are $0$ must have all powers beyond the 4th power as $0$.
### (c) Is it true that the cube of any such matrix (not just your example) must also be zero?
No.

<div style="page-break-after: always;"></div>

## (3) Let $G$ be the directed pentagon below, Let $A$ be the adjacency matrix of $G$. Describe all positive powers of $A$.
![alt text](<assignment 4/image.png>)\
$A^k=\begin{cases}\begin{pmatrix}0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\\0&0&0&0&1\\1&0&0&0&0\end{pmatrix}&k=5n+1,n\in\mathbb{\mathbb{N}}\\\begin{pmatrix}0&0&1&0&0\\0&0&0&1&0\\0&0&0&0&1\\1&0&0&0&0\\0&1&0&0&0\end{pmatrix}&k=5n+2,n\in{\mathbb{N}}\\\begin{pmatrix}0&0&0&1&0\\0&0&0&0&1\\1&0&0&0&0\\0&1&0&0&0\\0&0&1&0&0\end{pmatrix}&k=5n+3,n\in{\mathbb{N}}\\\begin{pmatrix}0&0&0&0&1\\1&0&0&0&0\\0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\end{pmatrix}&k=5n+4,n\in{\mathbb{N}}\\\begin{pmatrix}1&0&0&0&0\\0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\\0&0&0&0&1\end{pmatrix}&k=5n,n\in{\mathbb{N}}\end{cases}$\
*in this case $\mathbb{N}$ includes $0$.

<div style="page-break-after: always;"></div>

## (4) Let $G$ be the directed snail below, Let $A$ be the adjacency matrix of $G$. Describe all positive powers of $A$.
![alt text](<assignment 4/image1.png>)\
$A^k=\begin{cases}
\begin{pmatrix}
0&1&0\\
0&1&1\\
0&0&0
\end{pmatrix}&k=1\\
\begin{pmatrix}
0&1&1\\
0&1&1\\
0&0&0
\end{pmatrix}&k\in\mathbb{Z},k\ge2\\
\end{cases}$

<div style="page-break-after: always;"></div>

## (5) Let $(S,\preceq)$ be a finite poset. Let $G$ be the directed graph of the relation $\preceq$ and let $A$ be the adjacency matrix of $G$. Let $I$ be the identity matrix of the same size as $A$. True or false: some positive power of $A-I$ must be zero. If true, justify it. Otherwise give an example where no positive power of $A-I$ is zero.
subtracting any adjacency matrix $A$ by $I$ is simply the act of removing the reflexive edges from $G$, which can be treated as a conversion of $(S,\preceq)$ to $(S,\prec)$. Since the graph of $(S,\prec)$ is finite and asymetric, there is a maximum length path which exists. Therefore after a certain power $A-I$ is zero.