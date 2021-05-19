# Dynamic programming

## About project

Here I'm solving different tasks using DP.

## Tasks

### "Strong" grosshopper

#### What the task about?
You have N columns equidistant from each other. Each column has its value. Value can be called in a lot different ways(coin, price, etc.).
The grasshopper can only jump 1, 2 and 3 columns. The task is to find the most possible value that can be obtained by jumping to the end. Also you need to print number of columns
that you will jump to and count of this columns. If there are multiple solutions, you can print any

Input:                                                  
N - count of columns                                      
C - array of values. First and last columns have zeros <br />
I/O example:<br />
Input:<br />
5<br />
0 2 -3 5 0<br />
Output:<br />
7<br />
4<br />
0 1 3 4<br />

#### Solution
I'm using DP, that's why we need dp array. I added 2 extra columns to the begining to make our main loop work with the first and second column. The __main formula__ is dp[i] = 
max(dp[i-1], dp[i-2], dp[i-3]). All we need is to count all dp's from 3(first column + 2 extras) to n+2. The answer would be in a dp[n+1]

##### Complexity

T = O(n), n - count of columns <br />
M = O(n)
