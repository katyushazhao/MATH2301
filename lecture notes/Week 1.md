# Week 1 Notes
## Sets
### What is a set?
- A set is a collection of elements
    - unordered
    - no repetitions
- $x\in A$ or $x\notin A$
### The empty set
- $\empty = \{\}$
- Has no elements.
### Size/cardinality
- The size/cardinality of $A$ is the number of elements in $A$.
- Denoted by $|A|$ or #$A$. Write $|A|=\infty$ if #$A$ is infinite.
### Subsets and Supersets
- $A\subset B$ if $x\in A \implies x\in B$
- $\empty\subset A$ and $A\subset A$
- If $A\subset B$ then $|A|\le|B|$
### Operations
#### Product
$A\times B=\{(a,b)|a\in A, b\in B\}$\
$|A\times B|=|A|\times|B|$
#### Power Set
The power set of $A$ is the set of all subsets of $A$.\
$|P(A)|=2^{|A|}$
## Functions
A function $f:S\to T$ is a rule that assigns to every element of $S$ an element of $T$.\
The rule must be
- unambigious, and
- cover all elements of $S$.

We use $f(s)$ to denote the element of $T$ that $f$ assigns to the element $s$ of $S$.\
We call
- $S$: the source or domain of the function
- $T$: the target or co-domain of the function
- the range or image is a subset of the co-domain that are mapped to by $f$
### Properties of functions
#### Injectivity (one to one)
$f: S\to T$ is injective iff $f(x)=f(y)\implies x=y$\
if $f:S\to T$ is injective, $|S|\le|T|$
#### Surjectivity
$f: S\to T$ is surjective if $\forall y\in T, \exists x\in S|f(x)=y$\
if $f:S\to T$ is surjective, $|S|\ge|T|$
#### Bijectivity
$f: S\to T$ is bijective if it is both injective and surjective\
if $f:S\to T$ is bijective, $|S|=|T|$
### Number of functions
the number of functions $f:A\to B=|B|^{|A|}$\
if $|A|\le|B|$ there are $^{|B|}P_{|A|}$ injective funtions $f:A\to B$
### The inverse function
if $f:S\to T$ is a bijection, $f^{-1}:T\to S|t=f(s)\implies s=f^{-1}(y)$
## Relations
A relation on $S$ and $T$ is a subset $R\subset S\times T$\
if $(s,t\in R)$, then we think of $s$ as related to $t$ according to $R$.

$\{Relations\}=P(A\times B)$
###  The input/output relation of a function
An $f:S\to T$ gives a relation $R\subset S\times T$ given by $R=\{(s,t)|t=f(s)\}$\
This has an important property:\
$\forall s\in S, \exists!t\in T|(s,t)\in R$
### Reflexive Relations
$R\subset S\times S$ is reflexive if $\forall s\in S, (s,s)\in R$
### Symmetric Relations
$R\subset S\times S$ is symmetric if $\forall s,t\in S, (s,t)\in R\implies(t,s)\in R$
### Transitive Relations
$R\subset S\times S$ is transitive if $\forall a,b,c\in S, (a,b)\in R, (b,c)\in R \implies (a,c)\in R$