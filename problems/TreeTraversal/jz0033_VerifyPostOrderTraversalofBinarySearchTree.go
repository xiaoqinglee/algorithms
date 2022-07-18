package TreeTraversal

func verifyPostorder(postorder []int) bool {
	if len(postorder) <= 1 {
		return true
	}
	rightTreeFirstElementIndex := -1
	for i, val := range postorder {
		if i == len(postorder)-1 {
			break
		}
		if rightTreeFirstElementIndex == -1 && val > postorder[len(postorder)-1] {
			rightTreeFirstElementIndex = i
		}

		//注意，要对左右子树上所有的元素进行验证
		if rightTreeFirstElementIndex == -1 { // i是左子树的元素
			// do noting
		} else { // i是右子树的元素
			if val <= postorder[len(postorder)-1] {
				return false
			}
		}
	}
	okForLeftTree := true
	okForRightTree := true
	if rightTreeFirstElementIndex != -1 {
		okForLeftTree = verifyPostorder(postorder[:rightTreeFirstElementIndex])
		okForRightTree = verifyPostorder(postorder[rightTreeFirstElementIndex : len(postorder)-1])
	} else {
		okForLeftTree = verifyPostorder(postorder[:len(postorder)-1])
	}
	return okForLeftTree && okForRightTree
}
