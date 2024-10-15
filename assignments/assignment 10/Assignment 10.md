# (1)
Grundy's game is defined as follows. The starting position is some number of piles of berries. A move consists of taking one pile of berries, and dividing it into two non-empty piles of unequal sizes. For example, a pile of size 4 can only be split into 1/3, whereas a pile of 5 can be split either as 1/4 or as 2/3. The person who can't make a move loses: at this point, the game board will only have piles of size 1 or 2.\
Draw the game graph starting at the position 6, labelling each position as either N or P. Consider the piles to be unordered; that is, a position such as (1,4) is considered to be the same as the position (4,1).\
No justification is required.

---
![alt text](Q1.png)

# (2)
Recall poset chomp. We start with finite poset $S$. A move consists of removing an $a\in S$ together with all $b\in S$ with $a\preceq b$.\
Let $S$ be the divisor poset of 12 except the integer 1. So $S=\{2,3,4,6,12\}$ and $a\preceq b$ if $a$ divides $b$.\
Using strategic labeling on the game graph, determine if the following positions are N or P
---

![alt text](Q2.png)
## (a)
$\{3\}$

---
P
## (b)
$\{2,4\}$

---
N
## (c)
$\{2,3,4\}$

---
N
## (d)
$\{2,3,4,6,12\}$

---
N