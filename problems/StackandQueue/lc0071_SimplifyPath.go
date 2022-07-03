package StackandQueue

import (
	"strings"
)

func simplifyPath(path string) string {
	var folders []string
	var currentFolder []rune
	var currentFolderInString string

	processCurrentFolder := func() {
		currentFolderInString = string(currentFolder)
		currentFolder = currentFolder[:0]
		if currentFolderInString == "." {
			//do nothing
		} else if currentFolderInString == ".." { //弹栈
			top := folders[len(folders)-1]
			if top == "/" { //根目录
				//do nothing
			} else {
				folders = folders[:len(folders)-1]
			}
		} else { //压栈
			folders = append(folders, currentFolderInString)
		}
	}

	for i, char := range path {
		if char == '/' {
			if len(currentFolder) == 0 {
				if i == 0 { //根目录
					folders = append(folders, "/")
				} else if path[i-1] == '/' { //连续的'/'符号
					//do nothing
				}
			} else {
				processCurrentFolder()
			}
		} else {
			currentFolder = append(currentFolder, char)
		}
	}

	// The path does not end with a trailing '/'.
	if len(currentFolder) > 0 {
		processCurrentFolder()
	}

	if len(folders) > 0 && folders[0] == "/" {
		return "/" + strings.Join(folders[1:], "/")
	}
	return strings.Join(folders, "/")
}
