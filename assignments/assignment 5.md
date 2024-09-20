# MATH2301 Assignment 5
## (1) A directed graph is strongly connected if for every $i$ and $j$, there is a path from vertex $i$ to vertex $j$. True or False:
### (a) A graph with adjacency matrix $A$ is strongly connected iff $\exist n|A^{*n}$ with all entries equal to $[1]$.
Counterexample: the graph of $A=\begin{pmatrix}[0]&[1]&[0]\\ [0]&[0]&[1]\\ [1]&[0]&[0]\end{pmatrix}$ is strongly connected but there is no $n|A^{*n}=\begin{pmatrix}[1]&[1]&[1]\\ [1]&[1]&[1]\\ [1]&[1]&[1]\end{pmatrix}$\
$\therefore$ statement is false
### (b) A graph with adjacency matrix $A$ is strongly connected iff $\exist n|\sum_{i=0}^{n}A^{*i}$ with all entries equal to [1].
if the graph of $A$ is strongly connected then $\forall (i,j)\in A,\exists n|A_{(i,j)}^{*n}=[1]$ and since\
$[1]+[0]=[1]$ and $[1] + [1] = [1]$ then $\exists n|\sum_{i=0}^{n}A^{*i}=[1]$.\
$\therefore$ statement is true.

<div style="page-break-after: always;"></div>

## (2) Let $G$ be the graph of the relation $R=\{(a,b)|0\leq b-a\leq2\}$ on $S=\{1,2,3,4\}$. Draw $G$ and $G^+$. Write down the adjacency matrix of both graphs.
### $G$: 
![alt text](<assignment 5/image.png>)\
$A=\begin{pmatrix}1&1&1&0\\0&1&1&1\\0&0&1&1\\0&0&0&1\end{pmatrix}$
### $G^+:$
![alt text](<assignment 5/image1.png>)\
$A^+=\begin{pmatrix}1&1&1&1\\0&1&1&1\\0&0&1&1\\0&0&0&1\end{pmatrix}$

<div style="page-break-after: always;"></div>

## (3) Let $A$ be the boolean adjacency matrix of $G$. Prove that $G$ is transitive iff $A=A+A^{*2}$.
The adjacency matrix of any $G^+$ with $n$ nodes is $\sum^{n-1}_{i=1}A^{*i}$\
if $G$ is transitive then $G=G^+$\
$\implies A=A+\sum^{n-1}_{i=2}A^{*i}=A+A^{*2}$ (If $G$ is transitive, the matrix $A$ already includes paths of length 2. Thus, $A^{∗2}$ and beyond contribute nothing more to the sum.)\
$\therefore G=G^+\implies A=A+A^{*2}$

$A=A+A^{*2}$ implies every path of length $2$ (or any further length by recursiveness) between $(i,k)$ is already represented by a direct path. So all transitive connections are already in $A$ which means $G$ must be transitive.

$\therefore G=G^+\iff A=A+A^{*2}$

<div style="page-break-after: always;"></div>

## (4) Using the criterion in the previous problem, determine if the following adjacency matricies define transitive graphs:
### (a) $\begin{pmatrix}0&1\\1&0\end{pmatrix}$
$A^{*2}=\begin{pmatrix}[1]&[0]\\ [0]&[1]\end{pmatrix}$\
$A+A^{*2}=\begin{pmatrix}[1]&[1]\\ [1]&[1]\end{pmatrix}$\
$A+A^{*2}\neq A\implies G\neq G^+$
### (b) $\begin{pmatrix}1&1&0\\ 0&1&1\\ 0&0&1\end{pmatrix}$
$A^{*2}=\begin{pmatrix}[1]&[1]&[1]\\ [0]&[1]&[1]\\ [0]&[0]&[1]\end{pmatrix}$\
$A+A^{*2}=\begin{pmatrix}[1]&[1]&[1]\\ [0]&[1]&[1]\\ [0]&[0]&[1]\end{pmatrix}$\
$A+A^{*2}\neq A\implies G\neq G^+$
### (c) $\begin{pmatrix}0&1&1\\ 0&0&1\\ 0&0&0\end{pmatrix}$
$A^{*2}=\begin{pmatrix}[0]&[0]&[1]\\ [0]&[0]&[0]\\ [0]&[0]&[0]\end{pmatrix}$\
$A+A^{*2}=\begin{pmatrix}[0]&[1]&[1]\\ [0]&[0]&[1]\\ [0]&[0]&[0]\end{pmatrix}$\
$A+A^{*2}= A\implies G= G^+$

<div style="page-break-after: always;"></div>

### (5) Find the minimum cost of paths between any pair of verticies in the following graph. Assume every vertex has loops of length 0 (not shown).
![alt text](<assignment 5/image2.png>)\
$W=\begin{pmatrix}0&\infty&3&1\\5&0&\infty&\infty\\\infty&\infty&0&8\\3&2&\infty&0\end{pmatrix}$\
$W^{\odot 2}=\begin{pmatrix}
0&3&3&1\\
5&0&8&6\\
11&10&0&8\\
3&2&6&0
\end{pmatrix}$\
$W^{\odot 3}=\begin{pmatrix}
0&3&3&1\\
5&0&8&6\\
11&10&0&8\\
3&2&6&0
\end{pmatrix}$\
The matrix $W^{\odot 3}$ has entries with the lengths of the shortest paths between pairs of matricies.