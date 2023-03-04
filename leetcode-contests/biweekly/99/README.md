## 2578. Split With Minimum Sum
[Leetcode](https://leetcode.com/contest/biweekly-contest-99/problems/split-with-minimum-sum/) 

<div>
              <p>Given a positive integer <code>num</code>, split it into two non-negative integers <code>num1</code> and <code>num2</code> such that:</p>

<ul>
	<li>The concatenation of <code>num1</code> and <code>num2</code> is a permutation of <code>num</code>
	<ul>
		<li>In other words, the sum of the number of occurrences of each digit in <code>num1</code> and <code>num2</code> is equal to the number of occurrences of that digit in <code>num</code>.</li>
	</ul>
	</li>
	<li><code>num1</code> and <code>num2</code> can contain leading zeros.</li>
</ul>
<p>Return <em>the <strong>minimum</strong> possible sum of</em> <code>num1</code> <em>and</em> <code>num2</code>.</p>
<p><strong>Notes:</strong></p>
<ul>
	<li>It is guaranteed that <code>num</code> does not contain any leading zeros.</li>
	<li>The order of occurrence of the digits in <code>num1</code> and <code>num2</code> may differ from the order of occurrence of <code>num</code>.</li>
</ul>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> num = 4325
<strong>Output:</strong> 59
<strong>Explanation:</strong> We can split 4325 so that <code>num1 </code>is 24 and num2<code> is </code>35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> num = 687
<strong>Output:</strong> 75
<strong>Explanation:</strong> We can split 687 so that <code>num1</code> is 68 and <code>num2 </code>is 7, which would give an optimal sum of 75.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>10 &lt;= num &lt;= 10<sup>9</sup></code></li>
</ul>
</div>

## Solution

Task : Split the digits of a number into two groups in any order and the natural number formed by the digits in each group, should sum up to a minimum value.

Intuition: 
To get the minimum sum, both summands(numbers) should be possible minimum. 
To form the possible minimum number out of a set of digits, the most siginificant digit of the number gets the least valued digit and the least siginficant digit of the number should get the highest valued digit from the set of digits. In other words, the digits should be sorted in ascending order and then form the number.

We need to form two numbers out of a set of digits.
So, sort the digits in ascending order. Form the num1 and num2 using alternate digits in the sorted list. (left to right).

```
split_with_min_sum(num) {
    nums = []
    while num > 0
        nums.append(num % 10)
        num = num // 10
    nums.sort()
    n = len(nums)
    i = 0
    j = 0
    num_1 = 0
    num_2 = 0
    while i < n-1 and j < n
        num_1 = (num_1 * 10) + num_arr[i]
        num_2 = (num_2 * 10) + num_arr[j]
        i += 2
        j += 2
    if i < n
        num_1 = (num_1 * 10) + num_arr[i]
    return num_1 + num_2

}
```