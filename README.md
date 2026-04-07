# COP4533-PA3

Student Name: Leo Graham
UFID: 7279-6525

How to run code:
-
- After cloning the repo, navigate to the /src directory. In the /data directory there should be an example.in and example.out file. These files are what the program will be accessing and modifying. To run the program, simply type ``` python3 .\hvlcs.py ```.
  
Assumptions:
-
- If you wish to test different values, you will have to modify example.in in the afformentioned /data directory. Results can be seen in example.out.


Written Component:
- 
1.) <img width="1919" height="952" alt="Screenshot 2026-04-06 190505" src="https://github.com/user-attachments/assets/fab6b6f2-1bb2-4437-a46e-de94d21ad0dc" />

2.) <img width="1003" height="123" alt="Screenshot 2026-04-06 192745" src="https://github.com/user-attachments/assets/52800f18-6511-4ab3-938f-d97b049ebd4c" />

My recurrence equation demonstrates adeqate veracity as it covers the following cases:

Case 1: Both characters of i and j in the string match.
- In this case, we retreat back a single character in each string, and add the value from string A.

Case 2: Characters of i and j in the string do NOT match.
- We then find the maximum value of a valid subsequence by retreating one character back for each string , testing those items against eachother (one character back in string A vs j in string B, or one character back in string B vs i in string A.)

Both of these cases present the optimal method of finding the maximum value of the common subsequence between each string.

3.) 
```
    Input: n, m, A, B, associated values
    HVLCS(A, B, v):
    for i = 0 to n:
        OPT(i, 0) = 0
    for j = 0 to m:
        OPT(0, j) = 0
    for i = 1 to n:
        for j = 1 to m:
            if A[i] = B[j]:
                OPT[i, j] = OPT[i-1, j-1] + v(A[i])
            else:
                OPT[i, j] = max(OPT[i-1, j], OPT[i, j-1])

    return OPT[n, m]
```
The running time is O(nm)
