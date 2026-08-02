<h2><a href="https://www.geeksforgeeks.org/problems/sum-of-lengths-of-non-overlapping-subarrays2237/1?page=2&category=Arrays&company=Amazon,Microsoft,Google,Flipkart,Adobe,NPCI,Samsung&difficulty=Basic,Easy&status=unsolved&sortBy=submissions">Sum of Lengths of Non-Overlapping SubArrays</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p>Given an array <strong>arr[]</strong>, find the <strong>maximum</strong> sum of lengths of all non-overlapping subarrays with <strong>k</strong> as the maximum element in the subarray.</p>
<p><span style="font-size: 18px;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [2, 1, 4, 9, 2, 3, 8, 3, 4]. k = 4 
<strong>Output:</strong> 5
<strong>Explanation</strong>: </span><span style="font-size: 18px;">The subarrays [2, 1, 4] and [3, 4] have 4 as their maximum element. Their lengths are 3 and 2, giving a total length of 3 + 2 = 5. Hence, the answer is 5.</span>
</pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [1, 1, 2, 2, 55, 1, 2], k = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> </span><span style="font-size: 18px;">The valid subarrays with maximum element 2 are [1, 1, 2, 2] (length 4) and [1, 2] (length 2). Their total length is 4 + 2 = 6, so the answer is 6.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>arr[] = [4, 3, 1, 1, 10], k = 2
<strong>Output:</strong> 0<br><strong>Explanation:</strong> </span><span style="font-size: 18px;">There is no subarray whose maximum element is 2.</span></pre>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>6<br></sup></span><span style="font-size: 18px;">0 ≤ arr[i] ≤ 10<sup>6</sup><sup><br></sup></span><span style="font-size: 18px;">0 </span><span style="font-size: 18px;">≤ k&nbsp;</span><span style="font-size: 18px;">≤ 10<sup>6</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;