<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# MATH2301 Assignment 3
## (1) The units digit of a perfect square can only be $0,1,4,5,6$ or $9$. What are the possible units digits of
### (a) perfect cubes?
$0^3 = 0$\
$1^3 = 1$\
$2^3 = 8$\
$3^3 = 27$\
$4^3 = 64$\
$5^3 = 125$\
$6^3 = 216$\
$7^3 = 343$\
$8^3 = 512$\
$9^3 = 729$\
So all of the digits are possible.
### (b) perfect fourth powers?
$0^4 = 0$\
$1^4 = 1$\
$2^4 = 16$\
$3^4 = 81$\
$4^4 = 256$\
$5^4 = 625$\
$6^4 = 1296$\
$7^4 = 2401$\
$8^4 = 4096$\
$9^4 = 6561$\
So the possible digits are $0,1,5,6$\
This is because when considering the units digit of a power you are effectively working with modulo 10 so it is sufficient to check only the results for $[0,9]$.

<div style="page-break-after: always;"></div>

## (2) Let $S$ be the divisor poset of $100$. Suppose $f: S\to Z$ is a rank function such that $f(1)=0$.
### (a) Find $f(4)$ and $f(100)$
![alt text](<assignment 3/image.png>)\
$f(4)=2$\
$f(10)=2$
### (b) Find all $d\in S$ such that $f(d)=3$
$f^{-1}(3)=20,50$
## (3) Let $S=\{(a,b)\in\mathbb{Z}^2|a<b\}$. Define $\preccurlyeq$ on $S$ by the rule $(a,b)\preccurlyeq(c,d)$ if $c\leq a$ and $b\leq d$
### (a) Recall the notion of a locally finite poset from the workshop. Is $(S,\preccurlyeq)$ locally finite?
Yes because its on $\mathbb{Z}^2$
### (b) Recall the notion of a maximal chain from Friday's lecture. All maximal chains ending at $[0,10]$ have the same length, what is this length?
Example of a maximum chain: $[0,1],[0,2],[0,3],...,[0,10]$.
This chain has length 10.
### (c) Every element of $S$ has the same number of immediate successors. How many?
$[a,b]$ has immediate successors $[a-1,b]$ and $[a,b+1]$ so each element has 2 immediate successors.
## (4) Let $S=\{1,2,3,4\}$. Find all partial orders on $S$ in which $1$ is the minimum and $4$ is maximal and $2\preccurlyeq 3$.
![alt text](<assignment 3/image2.png>)