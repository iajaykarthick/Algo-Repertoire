
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
</div>

### 2580. Count Ways to Group Overlapping Ranges
[Solution](2580.%20Count%20Ways%20to%20Group%20Overlapping%20Ranges.md)
<div>
              <p>You are given a 2D integer array <code>ranges</code> where <code>ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> denotes that all integers between <code>start<sub>i</sub></code> and <code>end<sub>i</sub></code> (both <strong>inclusive</strong>) are contained in the <code>i<sup>th</sup></code> range.</p>

<p>You are to split <code>ranges</code> into <strong>two</strong> (possibly empty) groups such that:</p>

<ul>
	<li>Each range belongs to exactly one group.</li>
	<li>Any two <strong>overlapping</strong> ranges must belong to the <strong>same</strong> group.</li>
</ul>

<p>Two ranges are said to be <strong>overlapping</strong>&nbsp;if there exists at least <strong>one</strong> integer that is present in both ranges.</p>

<ul>
	<li>For example, <code>[1, 3]</code> and <code>[2, 5]</code> are overlapping because <code>2</code> and <code>3</code> occur in both ranges.</li>
</ul>

<p>Return <em>the <strong>total number</strong> of ways to split</em> <code>ranges</code> <em>into two groups</em>. Since the answer may be very large, return it <strong>modulo</strong> <code>10<sup>9</sup> + 7</code>.</p>
