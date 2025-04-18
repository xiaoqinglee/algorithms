package ArrayStackQueue

import (
	"math"
)

// https://leetcode.cn/problems/shortest-unsorted-continuous-subarray

// 在单调栈中，元素y想要入栈，单调栈的性质导致栈顶元素x被弹出，定义样一个事件叫做挤占。
// y叫做挤入元素，x叫做挤出元素。y可能会连续挤出多个元素。

func findUnsortedSubarray(nums []int) int {

	type ElemValAndIndex struct {
		Val   int
		Index int
	}

	//                   10
	//           9
	//         8
	//                 7
	//               6
	//             5
	//     4
	//       3
	//   2
	// 1
	// 考虑数组：
	// 1 2 4 3 8 9 5 6 7 10
	//     * -   -     *
	// 发生了3挤4、 5挤9、 5挤8三次挤占动作

	//nums subarray之外的元素是非递减的
	//subarray 所有元素大于等于subarray最小值min，小于等于subarray最大值max

	//从左到右扫描nums构建非递减栈
	//所有挤占事件中，
	//所有挤出元素中的最大值就是subarray最大值max，
	//所有挤入元素中的最小值就是subarray最小值min。
	//subarray的第一个元素是原数组从左到右第一个大于min的元素
	//subarray的最后一个元素是原数组从右到左第一个小于max的元素 (考虑[1,3,2,2,2])

	squeezeOutValMax := math.MinInt32 //subarray最大值
	squeezeInValMin := math.MaxInt32  //subarray最小值

	var ascNums []ElemValAndIndex
	for i, num := range nums {

		for len(ascNums) > 0 && ascNums[len(ascNums)-1].Val > num {

			squeezeOutValMax = max(squeezeOutValMax, ascNums[len(ascNums)-1].Val)
			squeezeInValMin = min(squeezeInValMin, num)

			ascNums = ascNums[:len(ascNums)-1]
		}

		ascNums = append(ascNums, ElemValAndIndex{Val: num, Index: i})
	}

	if squeezeOutValMax == math.MinInt32 {
		return 0
	}

	subarrayFirstElemIndex := -1
	subarrayLastElemIndex := -1
	for i, num := range nums {
		if num > squeezeInValMin {
			subarrayFirstElemIndex = i
			break
		}
	}
	for i := len(nums) - 1; i >= 0; i-- {
		if nums[i] < squeezeOutValMax {
			subarrayLastElemIndex = i
			break
		}
	}
	return subarrayLastElemIndex - subarrayFirstElemIndex + 1
}
