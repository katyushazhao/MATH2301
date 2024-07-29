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
Find $f(1)$ and $f(2)$. Justify your answers. 

$R$ is the I/O relation of $f(x)=\frac{3}{x}$, this is true because\
$\forall x\in S,\exists y\in S|y=\frac{3}{x}$\
$\therefore f(1)=3, f(3)=1$
## (2)
Let $R$ and $T$ be relations on $S$. Decide if the following are true or false. Justify your answers.
### (a) If $R$ and $T$ are symmetric then $R\cup T$ is symmetric
since $R$ is symmetric, $\forall a,b\in S,(a,b)\in R\implies (b,a)\in R$.\
This by extension means $(a,b)\in R \implies (b,a)\in R\cup T$. \
following simlarly for $T, (a,b)\in T \implies (b,a)\in R\cup T$.\
adding these together then $\forall a,b\in S,(a,b)\in R\cup T\implies(b,a)\in T\cup R$.\
$\therefore R\cup T$ is symmetric so the statement is true.
### (b) If $R$ and $T$ are transitive then $R \cup T$ is transitive
since $R$ is transitive, $\forall a,b,c\in S, (a,b)\in R, (b,c)\in R \implies (a,c)\in R$.\
This by extension means $(a,b)\in R,(b,c)\in R \implies (a,c)\in R\cup T$. \
following similarly for $T, (a,b)\in T,(b,c)\in T \implies (a,c)\in R\cup T$.\
adding these together then $\forall a,b,c\in S, (a,b)\in R\cup T, (b,c)\in R\cup T \implies (a,c)\in R\cup T$.
$\therefore R\cup T$ is transitive so the statement is true.
## (3) 
Consider the following graphs, for each one write down which of the following properties are satisfied by the graph: reflexivity, symmetry, transivity, being the I/O of a function.
### (a)
![alt text](<assignment 1/image.png>)\
This graph is reflexive.
### (b)
![alt text](<assignment 1/image-1.png>)\
This graph is symmetric and transitive.
### (c)
![alt text](<assignment 1/image-2.png>)\
This graph is the I/O of a function.
## (4)
Let $S=\mathbb{R}\times\mathbb{R}$. Define a relation $R$ on $S$ as follows:\
$R=\{(a,b),(c,d)|a+b=c+d\}$.
### (a) prove $R$ is an equivalence relation
$\forall(a,b)\in S, a+b=a+b$ so $R$ is reflexive.\
$\forall(a,b)\in S, a+b=c+d\implies c+d=a+b$ so $R$ is symmetric.\
$\forall ((a,b),(c,d),(e,f))\in S, a+b=c+d, c+d=e+f\implies a+b=e+f$ so $R$ is transitive.

Since $R$ is reflexive, symmetric and transitive, $R$ is an equivalence relation.
### (b) Describe the equivalence classes in words and draw sketches in $\mathbb{R}^2$ of the equivalance class of $(1,2)$ and of $(0,0)$.
$[x]_R=\{(a,b)\in\mathbb{R}^2\}|a+b=x$\
<div style="page-break-after: always;"></div>

for $(1,2)$
![alt text](<assignment 1/desmos-graph.png>)\
<div style="page-break-after: always;"></div>

for $(0,0)$
![alt text](<assignment 1/desmos-graph(1).png>)