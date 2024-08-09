<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# MATH2301 Assignment 2
## (1) Let $S$ be the set of squares on a standard $8\times 8$. Consider the following relations on $S$ and determine how many equivalence classes there are.

### (a) $B=\{(s,t)\in S\times S|t\}$ is reachable from $s$ by a sequence of zero or more bishop moves.
There are 2 equivalence classes - one for the black and one for the white tiles.
### (b) $R=\{(s,t)\in S\times S|t\}$ is reachable from $s$ by a sequence of zero or more rook moves.
There is 1 equivalence class containing the whole board.
### (c) $K=\{(s,t)\in S\times S|t\}$ is reachable from $s$ by a sequence of zero or more knight moves.
There is 1 equivalence class containing the whole board.

<div style="page-break-after: always;"></div>

## (2) Fix a modulus $d$. Recall that $\mathbb{Z}/d\mathbb{Z}$ is the set of equivalence classes of integers modulo $d$. Let us try to define the operation of exponentiation on $\mathbb{Z}/d\mathbb{Z}$ as follows. Given $A,B\in \mathbb{Z}/d\mathbb{Z}$, we pick an $a\in A$, a positive $b\in B$, and declare $A^B=[a^b]$. Is this operation well-defined? Justify your answer.
Choose $d=4$, $A=[2]=[6]$, $B=[1]=[5]$\
$2^1\mod 4=2$\
$6^5\mod 4=0$\
Since $[2]\neq[0]$, the result depends on the choice of representatives.
By counterexample, the operation of exponentiation is not well-defined on $\mathbb{Z}/d\mathbb{Z}$

<div style="page-break-after: always;"></div>

## (3) Consider modular arithmetic with the modulus $d=10$. For each equivalence class $[x]\in\mathbb{Z}/d\mathbb{Z}$ determine whether or not $[x]$ has the multiplicative inverse, and if yes, find the inverse. That is, figure out whether there is some $[y]$ such that $[x]\cdot[y]=[1]$.
$[0]$ has no inverse.\
$[1]\cdot[1]=[1]$\
$[2]$ has no inverse.\
$[3]\cdot[7]=[21]=[1]$\
$[4]$ has no inverse.\
$[5]$ has no inverse.\
$[6]$ has no inverse.\
$[7]\cdot[3]=[21]=[1]$\
$[8]$ has no inverse.\
$[9]\cdot[9]=[81]=[1]$

<div style="page-break-after: always;"></div>


## (4) Take the modulus to be $d=7$. Show that if $[3x]=5\mod 7$ then $x=4$
$[3]\cdot[x]=[5]$\
$[5]\cdot[3]\cdot[x]=[5]\cdot[5]$\
$[14]\cdot[x]=[25]$\
$[1]\cdot[x]=[4]$\
$[x]=[4]$