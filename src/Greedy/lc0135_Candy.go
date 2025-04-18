package Greedy

// https://leetcode.cn/problems/candy

//func candy(ratings []int) int {
//
//	//如果一个小孩a左右两边存在比他评分低的小孩b，那么a的糖果数A的确定依赖b的糖果数B的确定，A = B + 1。
//	//这样这就转换成了课程表先修课程拓补排序的问题。
//	//后序遍历依赖树即可。
//
//	if len(ratings) <= 1 {
//		return len(ratings)
//	}
//
//	childToSmallerRatingValueNeighbors := make(map[int][]int)
//	for child := range ratings {
//		if child != 0 {
//			if ratings[child-1] < ratings[child] {
//				childToSmallerRatingValueNeighbors[child] =
//					append(childToSmallerRatingValueNeighbors[child], child-1)
//			}
//		}
//		if child != len(ratings)-1 {
//			if ratings[child+1] < ratings[child] {
//				childToSmallerRatingValueNeighbors[child] =
//					append(childToSmallerRatingValueNeighbors[child], child+1)
//			}
//		}
//	}
//
//	// value 为 -1 代表还没有决定下来， value 为 非 -1 代表已经决定下来了。
//	childToChildCandyCount := make(map[int]int, len(ratings))
//	for child := range ratings {
//		childToChildCandyCount[child] = -1
//	}
//
//	var determineCandyCount func(childId int)
//	// 从名字看就应该设计成一个有副作用的函数，所以要确保该函数不会在同一个childId参数上多次调用。
//	// 既然我们决定设计成一个有副作用的函数，而且仅依靠副作用就能完成功能，所以就不让它返回值了。
//	// 设计函数让他不返回值能够更加防止我们错误地多次调用。
//	// 如果能把函数设计成幂等的，那就更好了，这样我们允许多次调用它，只要副作用幂等就可以。
//	determineCandyCount = func(childId int) {
//		if childToChildCandyCount[childId] != -1 {
//			return
//		}
//
//		smallerRatingValueNeighbors, ok := childToSmallerRatingValueNeighbors[childId]
//		if !ok {
//			childToChildCandyCount[childId] = 1
//			return
//		}
//		maxNeighborCandyCount := math.MinInt32
//		for _, neighbor := range smallerRatingValueNeighbors {
//			if childToChildCandyCount[neighbor] == -1 {
//				determineCandyCount(neighbor)
//			}
//			maxNeighborCandyCount = max(childToChildCandyCount[neighbor], maxNeighborCandyCount)
//		}
//		childToChildCandyCount[childId] = maxNeighborCandyCount + 1
//	}
//
//	for child := range ratings {
//		if childToChildCandyCount[child] == -1 {
//			determineCandyCount(child)
//		}
//	}
//
//	candyCountSum := 0
//	for _, candyCount := range childToChildCandyCount {
//		candyCountSum += candyCount
//	}
//	return candyCountSum
//}

func candy(ratings []int) int {

	//简单方法

	if len(ratings) <= 1 {
		return len(ratings)
	}

	//CandyCountOnlyConsideringLeftNeighbor
	left := make([]int, len(ratings))
	for child := 0; child < len(ratings); child += 1 {
		if child == 0 {
			left[child] = 1
		} else {
			if ratings[child-1] < ratings[child] {
				left[child] = left[child-1] + 1
			} else {
				left[child] = 1
			}
		}
	}
	//CandyCountOnlyConsideringRightNeighbor
	right := make([]int, len(ratings))
	for child := len(ratings) - 1; child >= 0; child -= 1 {
		if child == len(ratings)-1 {
			right[child] = 1
		} else {
			if ratings[child+1] < ratings[child] {
				right[child] = right[child+1] + 1
			} else {
				right[child] = 1
			}
		}
	}
	candyCount := make([]int, len(ratings))
	for child := 0; child < len(ratings); child += 1 {
		candyCount[child] = max(left[child], right[child])
	}

	candyCountSum := 0
	for _, candyCount_ := range candyCount {
		candyCountSum += candyCount_
	}
	return candyCountSum
}
