class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in range(0, len(coins)):
                if i >= coins[j]:
                    dp[i] = min(dp[i],1+dp[i-coins[j]])

        return -1 if dp[amount] == amount+1  else dp[amount]
        