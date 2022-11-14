<h2><a href="https://leetcode.com/problems/partition-array-according-to-given-pivot/">2161. Partition Array According to Given Pivot</a></h2><h3>Medium</h3><hr><div><p>You are given a <strong>0-indexed</strong> integer array <code style="background: rgb(0, 9, 15) !important;">nums</code> and an integer <code style="background: rgb(0, 9, 15) !important;">pivot</code>. Rearrange <code style="background: rgb(0, 9, 15) !important;">nums</code> such that the following conditions are satisfied:</p>

<ul>
	<li>Every element less than <code style="background: rgb(0, 9, 15) !important;">pivot</code> appears <strong>before</strong> every element greater than <code style="background: rgb(0, 9, 15) !important;">pivot</code>.</li>
	<li>Every element equal to <code style="background: rgb(0, 9, 15) !important;">pivot</code> appears <strong>in between</strong> the elements less than and greater than <code style="background: rgb(0, 9, 15) !important;">pivot</code>.</li>
	<li>The <strong>relative order</strong> of the elements less than <code style="background: rgb(0, 9, 15) !important;">pivot</code> and the elements greater than <code style="background: rgb(0, 9, 15) !important;">pivot</code> is maintained.
	<ul>
		<li>More formally, consider every <code style="background: rgb(0, 9, 15) !important;">p<sub>i</sub></code>, <code style="background: rgb(0, 9, 15) !important;">p<sub>j</sub></code> where <code style="background: rgb(0, 9, 15) !important;">p<sub>i</sub></code> is the new position of the <code style="background: rgb(0, 9, 15) !important;">i<sup>th</sup></code> element and <code style="background: rgb(0, 9, 15) !important;">p<sub>j</sub></code> is the new position of the <code style="background: rgb(0, 9, 15) !important;">j<sup>th</sup></code> element. For elements less than <code style="background: rgb(0, 9, 15) !important;">pivot</code>, if <code style="background: rgb(0, 9, 15) !important;">i &lt; j</code> and <code style="background: rgb(0, 9, 15) !important;">nums[i] &lt; pivot</code> and <code style="background: rgb(0, 9, 15) !important;">nums[j] &lt; pivot</code>, then <code style="background: rgb(0, 9, 15) !important;">p<sub>i</sub> &lt; p<sub>j</sub></code>. Similarly for elements greater than <code style="background: rgb(0, 9, 15) !important;">pivot</code>, if <code style="background: rgb(0, 9, 15) !important;">i &lt; j</code> and <code style="background: rgb(0, 9, 15) !important;">nums[i] &gt; pivot</code> and <code style="background: rgb(0, 9, 15) !important;">nums[j] &gt; pivot</code>, then <code style="background: rgb(0, 9, 15) !important;">p<sub>i</sub> &lt; p<sub>j</sub></code>.</li>
	</ul>
	</li>
</ul>

<p>Return <code style="background: rgb(0, 9, 15) !important;">nums</code><em> after the rearrangement.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre style="background: rgb(0, 9, 15) !important;"><strong>Input:</strong> nums = [9,12,5,10,14,3,10], pivot = 10
<strong>Output:</strong> [9,5,3,10,10,12,14]
<strong>Explanation:</strong> 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="background: rgb(0, 9, 15) !important;"><strong>Input:</strong> nums = [-3,4,3,2], pivot = 2
<strong>Output:</strong> [-3,2,4,3]
<strong>Explanation:</strong> 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code style="background: rgb(0, 9, 15) !important;">1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code style="background: rgb(0, 9, 15) !important;">-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code style="background: rgb(0, 9, 15) !important;">pivot</code> equals to an element of <code style="background: rgb(0, 9, 15) !important;">nums</code>.</li>
</ul>
</div>