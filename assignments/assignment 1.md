<script type="text/javascript" 
  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# MATH2301 Assignment 1
## (1)
Let $S=\mathbb{R}-\{0\}$ \
Define $R\subset S\times S$ as $\{(x,y)|xy=3\}$ and $R$ is the I/O relation of $f$. \
Find $f(1)$ and $f(3)$. Justify your answers. 

$R$ is the I/O relation of $f(x)=\frac{3}{x}$, this is true because\
$\forall x\in S,\exists y\in S|y=\frac{3}{x}$\
$\therefore f(1)=3, f(3)=1$

<div style="page-break-after: always;"></div>

## (2)
Let $R$ and $T$ be relations on $S$. Decide if the following are true or false. Justify your answers.
### (a) If $R$ and $T$ are symmetric then $R\cup T$ is symmetric
$(a,b)\in R\cup T\implies (a,b)\in R\lor(a,b)\in T$.\
Case 1: $(a,b)\in R\implies(b,a)\in R$ (as R is symmetric).\
since $R\subset R\cup T, (a,b)\in R\implies(b,a)\in R\cup T$\
Case 2: $(a,b)\in T\implies(b,a)\in T$ (as T is symmetric) \
since $T\subset R\cup T, (a,b)\in T\implies(b,a)\in R\cup T$\
$\therefore(a,b)\in R\cup T\implies (b,a)\in R\cup T$\
$\therefore$ the statement is true.
### (b) If $R$ and $T$ are transitive then $R \cup T$ is transitive
Take the example where $R$ is the relation $<$ and $T$ is the relation $>$ on $S=\mathbb{Z}$.\
$R$ is transitive as $\forall a,b,c\in S, a<b,b<c\implies a<c$.\
$T$ is transitive as $\forall a,b,c\in S, a>b,b>c\implies a>c$. \
Take the case where $a,b,c\in S, a=c>c$, in this case $a>b,b<c\in R\cup T$ however $(a,c)\notin R\cup T$.\
$\therefore$ by counterexample the statement is false.

<div style="page-break-after: always;"></div>

## (3) 
Consider the following graphs, for each one write down which of the following properties are satisfied by the graph: reflexivity, symmetry, transivity, being the I/O of a function.
### (a)
![alt text](<assignment 1/image.png>)\
This graph is reflexive and transitive.
### (b)
![alt text](<assignment 1/image-1.png>)\
This graph is symmetric.
It is not transitive as $(a,c),(c,a)\in R, (a,a)\notin R$
### (c)
![alt text](<assignment 1/image-2.png>)\
This graph is the I/O of a function.
<div style="page-break-after: always;"></div>

## (4)
Let $S=\mathbb{R}\times\mathbb{R}$. Define a relation $R$ on $S$ as follows:\
$R=\{(a,b),(c,d)|a+b=c+d\}$.
### (a) prove $R$ is an equivalence relation
$\forall(a,b)\in S, a+b=a+b$ so $R$ is reflexive.\
$\forall(a,b),(c,d)\in S, a+b=c+d\implies c+d=a+b$ so $R$ is symmetric.\
$\forall ((a,b),(c,d),(e,f))\in S, a+b=c+d, c+d=e+f\implies a+b=e+f$ so $R$ is transitive.

Since $R$ is reflexive, symmetric and transitive, $R$ is an equivalence relation.
<div style="page-break-after: always;"></div>

### (b) Describe the equivalence classes in words and draw sketches in $\mathbb{R}^2$ of the equivalance class of $(1,2)$ and of $(0,0)$.
$[x]_R=\{(a,b)\in\mathbb{R}^2\}|a+b=x$

for $(1,2)$
![alt text](<assignment 1/desmos-graph.png>)

for $(0,0)$
![alt text](<assignment 1/desmos-graph(1).png>)