## 61. Rotate List

[Leetcode](https://leetcode.com/problems/rotate-list/description/)

<div class="_1l1MA"><p>Given the <code>head</code> of a linked&nbsp;list, rotate the list to the right by <code>k</code> places.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 450px; height: 191px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5], k = 2
<strong>Output:</strong> [4,5,1,2,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 305px; height: 350px;">
<pre><strong>Input:</strong> head = [0,1,2], k = 4
<strong>Output:</strong> [2,0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 500]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
</ul>
</div>

### Solution 

Consider the list elements $l_1, l_2, l_3, \dots l_n$

When 
$k = 0,$ new head is $l_1$ ( no change )
$k = 1,$ new head is $l_n$ ( $l_n.next = l_1$ )
$k = 2,$ new head is $l_{n-1}$ ( $l_n.next = l_1$ )
$k = 3,$ new head is $l_{n-2}$ ( $l_n.next = l_1$ )
$\vdots$
$k = n-1,$ new head is $l_{2}$ ( $l_n.next = l_1$ )
$k = n,$ new head is $l_{1}$ ( no change )

$k$ can be greater than n and we need to start again in rotation.
In general, new head position is new_head_pos $= n - (k \mod n) + 1$.
There are some corner cases like $k = 0, (k \mod n) = 0 \text{ and } n = 1$. For all these corner cases, we don't need to change the head node.

#### Pseudocode
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head

        n = 0

        while curr:
            curr = curr.next
            n += 1

        if k == 0 or n < 2 or k % n == 0:
            return head
        
        new_head_pos = n - (k % n) + 1

        new_head = None
        
        curr = head
        node_pos = 1

        while curr:

            curr_next = curr.next

            if node_pos + 1 == new_head_pos:
                curr.next = None

            elif node_pos == new_head_pos:
                new_head = curr
            
            if node_pos == n:
                curr.next = head

            curr = curr_next
            node_pos += 1
            
        return new_head
```
