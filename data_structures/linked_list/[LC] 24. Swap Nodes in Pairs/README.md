## 24. Swap Nodes in Pairs

[Leetcode](https://leetcode.com/problems/swap-nodes-in-pairs/)

<div class="_1l1MA"><p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head. You must solve the problem without&nbsp;modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [2,1,4,3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> head = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the&nbsp;list&nbsp;is in the range <code>[0, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>
</div>

## Solution

Recurisvely go to tail with two pairs (to be swapped) in each level.

Swap pairs from the last and return new next node to predecessors.

Swap pairs and link them with new next node in each level.

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(node_1, node_2):
            if node_1 and not node_2:
                return node_1
            elif not node_1 and not node_2:
                return
            else:
                # find new next of current pair (node_1, node_2) after swap
                if node_2.next:
                    next_node = swap(node_2.next, node_2.next.next)
                else:
                    next_node = swap(None, None)
                
                node_2.next = node_1
                node_1.next = next_node
                return node_2
        if head:
           head = swap(head, head.next)
        return head

            

```