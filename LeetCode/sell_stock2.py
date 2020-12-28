from typing import List

# 买卖股票的最佳时机2
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
# 思路：简单动态规划


def max_profit(prices: List[int]) -> int:

    if not prices:
        return 0

    n = len(prices)
    dp = [[0, 0] for i in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0]

    for i in range(1, n):
        # dp[i][0] 表示第 i 天交易后手里没有股票的最大利润
        # 取前一天持有+今日股价、前一天未持有 两者的最大值
        dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
        # dp[i][1] 表示第 i 天交易后手里持有股票的最大利润
        # 取前一天未持有-今日买入价、前一天已持有 两者的最大值
        dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])

    # dp[n-1][0] 一定比 dp[n-1][1] 大
    return dp[n - 1][0]


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))
