package HashTable

func intersection(nums1 []int, nums2 []int) []int {

	if len(nums1) < len(nums2) {
		nums2, nums1 = nums1, nums2
	}
	// now nums2 is shorter

	numIsShared := make(map[int]bool)
	var result []int

	for _, num := range nums2 {
		numIsShared[num] = false
	}

	for _, num := range nums1 {
		if _, ok := numIsShared[num]; ok {
			numIsShared[num] = true
		}
	}
	for num, isShared := range numIsShared {
		if isShared {
			result = append(result, num)
		}
	}
	return result
}
