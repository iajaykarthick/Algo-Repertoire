
### 2578. Split With Minimum Sum

[Solution](2578.%20Split%20With%20Minimum%20Sum.md)
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
</div>

### 2579. Count Total Number of Colored Cells
[Solution ](2579.%20Count%20Total%20Number%20of%20Colored%20Cells.md)

<div class="question-content default-content">
              <p>There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer <code>n</code>, indicating that you must do the following routine for <code>n</code> minutes:</p>
<ul>
	<li>At the first minute, color <strong>any</strong> arbitrary unit cell blue.</li>
	<li>Every minute thereafter, color blue <strong>every</strong> uncolored cell that touches a blue cell.</li>
</ul>
<p>Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.</p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png" style="width: 500px; height: 279px;">
<p>Return <em>the number of <strong>colored cells</strong> at the end of </em><code>n</code> <em>minutes</em>.</p>