## Linear Recurrences
Each term of a sequence is a linear function of earlier terms in the sequence.

$\Rightarrow$ $a_{n} = f(a_{n-1}, ..., a_{n-k}) = c_1 a_{n-1} + ... + c_k a_{n-k} + f(n)$ where $c_i, f(n)$ are real numbers.

The order of linear recurrence relation is determined by "k". The $a_n$ is defined in terms of previous "k" terms of the sequence, so its degree is "k".

This type of recurrence comes with "k" base cases that specify the values for $a_0, a_1, ... a_{k-1}$.

Two types:
- Linear homogeneous recurrences
    - if f(n) = 0

- Linear non-homogeneous recurrences