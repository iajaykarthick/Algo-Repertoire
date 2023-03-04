# 15-4 Printing neatly [CLRS] 

Consider the problem of neatly printing a paragraph with a monospaced font (all characters having the same width) on a printer. The input text is a sequence of n words of lengths $l_1, l_2, \dots l_n$, measured in characters. We want to print this paragraph neatly on a number of lines that hold a maximum of M characters each. 

Our criterion of “neatness” is as follows. If a given line contains words i through j , where $i \leq j$ , and we leave exactly one space between words, the number of extra space characters at the end of the line is $M - j + i - \displaystyle\sum_{k=i}^{l} l_k$, which must be nonnegative so that the words fit on the line. We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines. 

Give a dynamic-programming algorithm to print a paragraph of n words neatly on a printer. Analyze the running time and space requirements of your algorithm.


### Optimal Substructure Property
The problem contains optimal substrcutre as follows:

Consider there exists optimal solution of arranging the n words $1, 2, \dots n$   with minimum cost $(M - j + i - \displaystyle\sum_{k=i}^{l} l_k)^3$ over all the lines.

Obviously the last line in the optimal solution ends with word $n$. Let the starting word of the last optimal line be word $m$.

Hence the last optimal line looks like $word_m word_{m+1} \dots word_n$.
Now, if we remove the last optimal line from the optimal solution, the optimal solution is left with the words $1$ through word $m-1$ in the optimal arrangment with minimum cost. In other words, it is the optimal solution to the subproblem of size $m-1$.

Thus, there exists the optimal substructure. 

### Recursive function

Let $C[j]$ be the minimum cost of printing the words $1$ through $j$.  




