class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        numOfCoins = [amount + 1] * (amount + 1)
        numOfCoins[0] = 0 

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    numOfCoins[a] = min(numOfCoins[a], 1 + numOfCoins[a - c])
                
        return numOfCoins[amount] if numOfCoins[amount] != (amount + 1) else -1