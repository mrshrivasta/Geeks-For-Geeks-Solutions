<h2><a href="https://www.geeksforgeeks.org/problems/chocolate-station2951/1?page=2&category=Arrays&company=Amazon,Microsoft,Google,Flipkart,Adobe,NPCI,Samsung&difficulty=Basic,Easy&status=unsolved&sortBy=submissions">Chocolate Station</a></h2><h3>Difficulty Level : Difficulty: Easy</h3><hr><div class="problems_problem_content__Xm_eO" style="--text-color: var(--problem-text-color);"><p><span style="font-size: 14pt;">Given an integer array <strong>arr[]</strong>, where arr[i] represents the number of chocolates associated with the i-th station. </span></p>
<ul>
<li><span style="font-size: 14pt;">Geek travels from station <strong>1</strong> to station <strong>n</strong>. </span></li>
<li><span style="font-size: 14pt;">In the move from </span><span style="font-size: 14pt;"><strong>i</strong> to <strong>i + 1</strong>, the number of chocolates adjust by <strong>arr[i] - arr[i + 1]</strong>. A positive value means gains, while a negative value means loses. </span></li>
<li><span style="font-size: 14pt;">Geek can move to the next station only if the number of chocolates he currently has is non-negative. </span></li>
<li><span style="font-size: 14pt;">Initially, he has <strong>0</strong> chocolates, but he may buy any number before starting his journey. Each chocolate costs <strong>price</strong> dollors.</span></li>
</ul>
<p><span style="font-size: 14pt;">Return the <strong>minimum</strong> cost required for Geek to reach station <strong>n</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Examples:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [1, 2, 3], price = 10
<strong>Output: </strong>30
<strong>Explanation</strong>: Geek buys 1 chocolate initially. He loses 1 chocolate while moving from station 1 to 2 and another 1 while moving from station 2 to 3. Thus, he buys a total of 3 chocolates. Cost = 3 × 10 = 30.</span></pre>
<pre><span style="font-size: 14pt;"><strong>Input: </strong>arr[] = [4, 1, 5, 2], price = 5
<strong>Output:</strong> 25
<strong>Explanation</strong>: <br></span><span style="font-size: 18.6667px;">Geek buys 4 chocolates initially. While moving from station 1 to 2, he gains 3 chocolates. Moving from station 2 to 3, he loses 4 chocolates, leaving him with -1 chocolate. So, he needs to buy 1 additional chocolate initially. Thus, the minimum chocolates required are 5, and the minimum cost is 5 × 5 = 25.</span></pre>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ arr.size() ≤ 10<sup>5</sup><sup><br></sup>1 ≤ arr[i] ≤ 100</span><br><span style="font-size: 14pt;">1 ≤ price ≤ 100</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;