<h2><a href="https://leetcode.com/problems/shuffle-string/">1528. Shuffle String</a></h2><h3>Easy</h3><hr><div><p>You are given a string <code style="background: rgb(0, 9, 15) !important;">s</code> and an integer array <code style="background: rgb(0, 9, 15) !important;">indices</code> of the <strong>same length</strong>. The string <code style="background: rgb(0, 9, 15) !important;">s</code> will be shuffled such that the character at the <code style="background: rgb(0, 9, 15) !important;">i<sup>th</sup></code> position moves to <code style="background: rgb(0, 9, 15) !important;">indices[i]</code> in the shuffled string.</p>

<p>Return <em>the shuffled string</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/09/q1.jpg" style="width: 321px; height: 243px;">
<pre style="background: rgb(0, 9, 15) !important;"><strong>Input:</strong> s = "codeleet", <code style="background: rgb(0, 9, 15) !important;">indices</code> = [4,5,6,7,0,2,1,3]
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong> As shown, "codeleet" becomes "leetcode" after shuffling.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre style="background: rgb(0, 9, 15) !important;"><strong>Input:</strong> s = "abc", <code style="background: rgb(0, 9, 15) !important;">indices</code> = [0,1,2]
<strong>Output:</strong> "abc"
<strong>Explanation:</strong> After shuffling, each character remains in its position.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code style="background: rgb(0, 9, 15) !important;">s.length == indices.length == n</code></li>
	<li><code style="background: rgb(0, 9, 15) !important;">1 &lt;= n &lt;= 100</code></li>
	<li><code style="background: rgb(0, 9, 15) !important;">s</code> consists of only lowercase English letters.</li>
	<li><code style="background: rgb(0, 9, 15) !important;">0 &lt;= indices[i] &lt; n</code></li>
	<li>All values of <code style="background: rgb(0, 9, 15) !important;">indices</code> are <strong>unique</strong>.</li>
</ul>
</div>