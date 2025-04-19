package PrefixSum

import "fmt"

// https://leetcode.cn/problems/subarray-sum-equals-k
// 参考 lc 0001
func subarraySum(nums []int, k int) int {
	count := 0

	//某个数组[x+1..y]的元素和K 加 数组[0..x]的元素和X 等于 数组[0..y]的元素和Y。
	//K + X = Y -> Y - K = X
	//数组[0..i]叫做原数组的prefix数组

	//向后遍历数组，每当得到一个新的prefix数组，
	//把该prefix数组的元素和X作为哈希的key，该prefix数组的最后一个元素的索引追加到key对应的value数组中。
	//存在多个prefix数组的和相等的情景。
	sumToLastIndexes := make(map[int][]int, len(nums))

	sum := 0
	sumToLastIndexes[sum] = append(sumToLastIndexes[sum], -1)
	//sumToLastIndexes:
	//map[0:[-1]]
	fmt.Println("sumToLastIndexes:")
	fmt.Println(sumToLastIndexes)

	for i, num := range nums {
		sum += num
		if lastElementIndexes, ok := sumToLastIndexes[sum-k]; ok {
			for _, lastElementIndex := range lastElementIndexes {
				fmt.Printf("找到子数组nums[%v..%v]: %v\n",
					lastElementIndex+1, i, nums[lastElementIndex+1:i+1])
			}
			count += len(lastElementIndexes)
		}
		sumToLastIndexes[sum] = append(sumToLastIndexes[sum], i)
	}
	return count
}
