package DynamicProgramming

// https://leetcode.cn/problems/combination-sum/
func combinationSum(candidates []int, target int) [][]int {

	// 题目背景可以说和 lc0322 找零钱一模一样，但是本题目要求输出所有的找零方案
	// 完全背包问题

	// 枚举所有可行的找零方案，需要回溯，（能做到剪枝的话更好）

	var combinations [][]int
	var candidateCountList [][]int
	candidateCount_ := make([]int, len(candidates))

	var traverse func(candidateCount []int, fixedFirstNCount int, accumulatedSum int)
	traverse = func(candidateCount []int, fixedFirstNCount int, accumulatedSum int) {
		if fixedFirstNCount == len(candidateCount) {
			if accumulatedSum == target {
				viableCandidateCount := make([]int, len(candidateCount), len(candidateCount))
				copy(viableCandidateCount, candidateCount)
				candidateCountList = append(candidateCountList, viableCandidateCount)
			}
			return
		}
		count := 0
		for {
			candidateCount[fixedFirstNCount] = count
			newAccumulatedSum := accumulatedSum + candidates[fixedFirstNCount]*count
			if newAccumulatedSum > target {
				break
			}
			traverse(candidateCount, fixedFirstNCount+1, newAccumulatedSum)
			count += 1
		}
	}

	traverse(candidateCount_, 0, 0)

	for _, candidateCount := range candidateCountList {
		var combination []int
		for candidateIndex, count := range candidateCount {
			if count == 0 {
				continue
			}
			for nTimes := 1; nTimes <= count; nTimes += 1 {
				combination = append(combination, candidates[candidateIndex])
			}

		}
		combinations = append(combinations, combination)
	}

	return combinations
}
