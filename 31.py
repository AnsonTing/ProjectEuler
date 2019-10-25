# Project Euler No. 31

def solution(coins, target):
    if not coins:
        return 0
    coins.sort()
    dp = []
    for _ in range(len(coins)):
        dp.append([1] + [None] * target)
    for i in range(1, target+1):
        if i % coins[0] == 0:
            dp[0][i] = 1
        else:
            dp[0][i] = 0
    for i in range(1, len(coins)):
        for j in range(1, target+1):
            if j < coins[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
    return dp[-1][-1]

print solution([1,2,5,10,20,50,100,200], 200)
