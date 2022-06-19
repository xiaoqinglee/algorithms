package problems

func combinationSum(candidates []int, target int) [][]int {

	// 题目背景可以说和 lc0322 找零钱一模一样，但是本题目要求输出所有的找零方案
	// 注意所有可行的找零方案数并不是 lc0322 中所有子问题的值的累加和，因为 lc0322 中的子问题相互重复

	// 枚举所有可行的找零方案，需要回溯，（能做到剪枝的话更好）

	var combinations [][]int
	var candidateCountResults [][]int

	var traverse func(candidateCount []int, fixedFirstNCount int, accumulatedSum int)

	candidateCount_ := make([]int, len(candidates))
	traverse = func(candidateCount []int, fixedFirstNCount int, accumulatedSum int) {
		if fixedFirstNCount == len(candidateCount) {
			if accumulatedSum == target {
				count := make([]int, len(candidateCount), len(candidateCount))
				copy(count, candidateCount)
				candidateCountResults = append(candidateCountResults, count)
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

	for _, candidateCount := range candidateCountResults {
		var combination []int
		for i, count := range candidateCount {
			if count == 0 {
				continue
			}
			for nTimes := 1; nTimes <= count; nTimes += 1 {
				combination = append(combination, candidates[i])
			}

		}
		combinations = append(combinations, combination)
	}

	return combinations
}
