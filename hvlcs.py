def solve():
    # Reading and parsing input
    with open("example.in", "r") as f:
        data = f.read().split('\n')
    
    idx = 0
    
    K = int(data[idx]); idx += 1
    
    char_value = {}
    for _ in range(K):
        parts = data[idx].split(); idx += 1
        char_value[parts[0]] = int(parts[1])
    
    A = data[idx].strip(); idx += 1
    B = data[idx].strip(); idx += 1
    
    n, m = len(A), len(B)
    
    # Max value of common subsequence
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + char_value.get(A[i-1], 0)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtracking
    result = []
    i, j = n, m
    while i > 0 and j > 0:
        if A[i-1] == B[j-1]:
            result.append(A[i-1])
            i -= 1; j -= 1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    result.reverse()
    
    #Output the result
    with open("example.out", "w") as f:
        f.write(f"{dp[n][m]}\n")
        f.write(''.join(result) + "\n")

solve()