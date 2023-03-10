### 2. Add Two Numbers

[Leetcode](https://leetcode.com/problems/add-two-numbers/) 

<img src="https://img.shields.io/badge/Medium-FFB84C.svg"> 

<div class="_1l1MA"><p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;">
<pre><strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 9</code></li>
	<li>It is guaranteed that the list represents a number that does not have leading zeros.</li>
</ul>
</div>

### Solution

Intuition : Recursively add corresponding digits in both the lists and the carry digit if any. Once reach the base, return the node with the result digit as the value and catch it by the next pointer of the previous recursive call's node.

```python
 def add(l1, l2, carry):
	if l1 is None and l2 is None and carry == 0:
		return
	
	res = carry
	l1_next = None
	l2_next = None
	
	if l1:
		l1_next = l1.next
		res += l1.val 
	if l2:
		l2_next = l2.next
		res += l2.val

	carry = res // 10
	res = res % 10

	node = ListNode()
	node.val = res
	node.next = add(l1_next, l2_next, carry)

	return node

add(l1, l2, 0)
```
