package ArrayStackQueue

import (
	"strings"
)

// https://leetcode.cn/problems/simplify-path
func simplifyPath(path string) string {
	var folders []string
	var currentFolderNameBuff []rune

	processCurrentFolderName := func() {
		currentFolderName := string(currentFolderNameBuff)
		if currentFolderName == "." {
			//do nothing
		} else if currentFolderName == ".." { //弹栈
			if len(folders) == 0 {
				panic("invalid input")
			}
			top := folders[len(folders)-1]
			if top == "/" { //根目录
				//do nothing
			} else {
				folders = folders[:len(folders)-1]
			}
		} else { //压栈
			folders = append(folders, currentFolderName)
		}
		currentFolderNameBuff = currentFolderNameBuff[:0]
	}

	for i, char := range path {
		if char == '/' && i == 0 { //根目录
			folders = append(folders, "/")
			continue
		}
		if char == '/' && i > 0 && path[i-1] == '/' { // 连续的 '/'
			// do nothing
			continue
		}
		if char == '/' {
			processCurrentFolderName()
		} else {
			currentFolderNameBuff = append(currentFolderNameBuff, char)
		}
	}

	// when the path does not end with a trailing '/'
	if len(currentFolderNameBuff) > 0 {
		processCurrentFolderName()
	}

	if len(folders) > 0 && folders[0] == "/" {
		return "/" + strings.Join(folders[1:], "/")
	}
	return strings.Join(folders, "/")
}
