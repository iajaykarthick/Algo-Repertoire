## Linear Recurrences
Each term of a sequence is a linear function of earlier terms in the sequence.

$\Rightarrow$ $a_{n} = f(a_{n-1}, ..., a_{n-k}) = c_1 a_{n-1} + ... + c_k a_{n-k} + f(n)$ where $c_i, f(n)$ are real numbers.

The order of linear recurrence relation is determined by "k". 

The $a_n$ is defined in terms of previous "k" terms of the sequence, so its degree is "k".

This type of recurrence comes with "k" base cases that specify the values for $a_0, a_1, ... a_{k-1}$.

Order | $a_n$ |
--- | --- | 
First order | f($a_{n-1}$) |
Second order | f($a_{n-1}, a_{n-2}$) |
Third order | f($a_{n-1}, a_{n-2}, a_{n-3}$) |
$k^{th}$ order | f($a_{n-1}, a_{n-2}, a_{n-3}, ... , a_{n-k}$) |

Two types:
- ## Linear homogeneous recurrences
    A linear recurrence is homogeneous if f(n) = 0

    $a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k}$                (1)

    where $c_1, c_2, .. c_k$ are real numbers and $c_k \ne 0$

- **Examples**

    * $a_n = a_{n-1} + a_{n-2}$ (order 2)
    * $a_n = a_{n-6}$ (order 6)

- **Not linear and not linear homogeneous (Examples)**
    * $a_n = a_{n-2} + a_{n-4}^2$ is not linear
    * $a_n = a_{n-1} + 1$ is not linear homogeneous
    * $a_n = na_{n-1}$ is not linear as it doesn't have constant coefficient


### Solving Linear Homogeneous Recurrences
A closed formula for a sequence $(a_n)_{n \in N}$ is a formula for  using a fixed finite number of operations on $n$.



- ## Linear non-homogeneous recurrences