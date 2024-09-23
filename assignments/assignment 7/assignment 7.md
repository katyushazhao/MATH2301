# (1) 
Let $\Sigma=\{0,1\}$. For each language $L$ described below, write down a regular expresion $r$ such that $L(r)=L$. That is the strings of $\Sigma^*$ that match $r$ are exactly the strings of $L$. Be careful to make sure that nothing else matches the regular expression you write down! Justification is not required.
## (a) $L=\{w\in\Sigma^*|w\text{ starts with a }1\}$
$r=1(1|0)^*$
## (b) $L=\{w\in\Sigma^*|w\text{ any ones in }w\text{ are next to eachother in a single block}\}$
$r=(0)^*(1)^*(0)^*$
## (c) $L=\{w\in\Sigma^*|w\text{ contains an even number of zeroes}\}$
$r=((00)|1)^*$
# (2) 
Let $\Sigma=\{a,b,c\}$. For each regular expression $r$ written below, describe in words the language $L(r)$. Justification not required.
## (a) $r=(\epsilon|bc|c)(abc)^*(\epsilon|a|ab)$
$L=\{w\in\Sigma^*|\text{ every letter in  }w\text{ is always followed by the next letter in the order of }\Sigma\}$
## (b) $r=((b|c|\epsilon)^*a(b|c|\epsilon)^*a(b|c|\epsilon)^*)^*$
$L=\{w\in\Sigma^*|\text{ every non-} a\text{ letter in  }w\text{ is always followed by }a\text{ unless it is the final letter}\}$
# (3)
Let $\Sigma=\{0,1\}$ and $L$ be the language
$$
L = w|\text{ the number of occurences of } 01 \text{ in }w\text{ is equal to the number of occurences of }10
$$
For example, the word $010$ is in $L$ because it has one occurences of $01$ and one of $10$. The word $01101$ is not in $L$ because it has $2$ occurences of $01$ but only one of $10$. Does there exist a regular expression $r$ such that $L=L(r)$? If yes, find one. If not, explain why not.

---
$r=(10(0^*)1|01(1^*)0)^*$
# (4) 
Let $L\subseteq\Sigma^*$ be a language. The compliment of $L$, denoted $L^c$, is the compliment of $L$ in $\Sigma^*$. That is, for every $w\in\Sigma^*$, we have $w\in L^{c}$ if and only if $w\notin L$
## (a) 
Given a DFA $M$ recognising a language $L=L(M)$, explain how to construct a DFA $M'$ such that $L(M')=L^{c}$

---
Let $M$ have:
- states $Q$
- start state $q_0\in Q$
- accept states $A\subseteq Q$ and, 
- transition function $\delta:Q\times\Sigma\to Q$\

then $M'$ must have:
- states $Q$
- start state $q_0$
- accept states $Q\setminus A$ and,
- transition function $\delta$
## (b) 
Construct a DFA recognising the following language:
$$
L = \{w\in\Sigma^{*}|\text{ every odd position of }w\text{ is }1\}
$$
Justification not required.

---
Let DFA $M$ recognise $L=L(M)$, $M$ has:
- states $Q=\{q_0,q_1,q_2\}$
- start state $q_0\in Q$
- accept states $A=\{q_0,q_1\}$ and, 
- transition function $\delta:$
  |Input State|Letter|Output State|
  |---|---|---|
  |$q_0$|$1$|$q_1$|
  |$q_0$|$a\in\Sigma,a\neq 1$|$q_2$