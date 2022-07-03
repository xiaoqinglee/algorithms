package TwoPointers

func ContainerWithMostWater(height []int) int {

	min := func(a, b int) int {
		if a < b {
			return a
		} else {
			return b
		}
	}

	if len(height) <= 1 {
		panic("Invalid Input height")
	}
	leftIndex := 0
	rightIndex := len(height) - 1
	maxArea := 0
	for {
		if leftIndex == rightIndex {
			break
		}
		area := (rightIndex - leftIndex) * min(height[leftIndex], height[rightIndex])
		if area > maxArea {
			maxArea = area
		}
		if height[leftIndex] < height[rightIndex] {
			leftIndex += 1
		} else {
			rightIndex -= 1
		}
	}
	return maxArea
}
