class Solution:
    def minimum_sum(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        return dp[0]


solution = Solution()
result = solution.minimum_sum(
    triangle=[
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3],
    ]
)

print(result)
