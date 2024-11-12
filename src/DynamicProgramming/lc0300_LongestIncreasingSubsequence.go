package DynamicProgramming

// https://leetcode.cn/problems/longest-increasing-subsequence
func lengthOfLIS(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}

	result := 1

	//dp[i]的值是以nums[i]作为最后一个元素的所有递增子序列中元素个数最大的那个递增子序列的元素数
	dp := make([]int, len(nums))
	for i := range dp {
		dp[i] = 1
	}

	for i := range nums {
		if i == 0 {
			dp[i] = 1
		} else {
			for iPrev := 0; iPrev < i; iPrev += 1 {
				if nums[iPrev] < nums[i] {
					dp[i] = max(dp[iPrev]+1, dp[i])
				}
			}
		}

		if dp[i] > result {
			result = dp[i]
		}
	}

	return result
}
